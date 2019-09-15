#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@ Desc:
    Main Code flow
    1) data pre-handling
        a) search and collect all matched data files: .csv, .log ...
        b) check data integrity of each file
    2) data parsing
        a) extract data based on fields
        b) filter out usable data fields
    3) data computation
    4) data to excel or visualization
@ requirement:
    1) python3
    2) modules:
           pandas,
           xlrd: read excel data
           xlwt: write to excel
           openpyxl: read/write Excel 2010 xlsx/xlsm files


@ author: byron
@ Date: 2019-08-30
@ History: 
"""

import argparse
import os
import logging
import re
import pandas as pd
from collections import OrderedDict

DATE_FMT = '%y%m%d %H:%M:%S'
LOG_FMT = "%(asctime)s %(filename)s %(levelname)s: %(message)s"
logging.basicConfig(level=logging.DEBUG, format=LOG_FMT, datefmt=DATE_FMT)
logger = logging.getLogger("iostat_viewer")

DATA_FIELDS_MAP = {
    "seq_read": ['Block size', 'IO type', 'WR/RD', 'Jobs', 'Queue Depth', 'Bandwidth(kB/s)', 'Lantency(us)'],
    "seq_write": ['Block size', 'IO type', 'WR/RD', 'Jobs', 'Queue Depth', 'Bandwidth(kB/s)', 'Lantency(us)'],
    "seq_mix": ['Block size', 'IO type', 'Queue Depth', 'Bandwidth(kB/s)', 'Lantency(us)',
                'Bandwidth(kB/s).1', 'Lantency(us).1'],
    "rand_read": ['Block size', 'IO type', 'WR/RD', 'Jobs', 'Queue Depth', 'IOPS', 'Lantency(us)'],
    "rand_write": ['Block size', 'IO type', 'WR/RD', 'Jobs', 'Queue Depth', 'IOPS', 'Lantency(us)'],
    "rand_mix": ['Block size', 'IO type', 'Queue Depth', 'IOPS', 'Lantency(us)', 'IOPS.1', 'Lantency(us).1']
}

EXL_PARAM_MAP = {
    "seq_read": {"Disks-Bandwidth": ['Block size', 'IO type', 'WR/RD', 'Jobs', 'Queue Depth', 'Bandwidth(kB/s)'],
                 "Disks-Latency": ['Block size', 'IO type', 'WR/RD', 'Jobs', 'Queue Depth', 'Lantency(us)']},
    "seq_write": {"Disks-Bandwidth": ['Block size', 'IO type', 'WR/RD', 'Jobs', 'Queue Depth', 'Bandwidth(kB/s)'],
                  "Disks-Latency": ['Block size', 'IO type', 'WR/RD', 'Jobs', 'Queue Depth', 'Lantency(us)']},
    # 'Bandwidth(kB/s)': ['read', 'write']
    "seq_mix": {"Disks-Bandwidth": ['Block size', 'IO type', 'Queue Depth', 'read', 'write'],
                # Latency: ['read', 'write']
                "Disks-Latency": ['Block size', 'IO type', 'Queue Depth', 'read', 'write']},

    "rand_read": {"Disks-IOPS": ['Block size', 'IO type', 'WR/RD', 'Jobs', 'Queue Depth', 'IOPS'],
                  "Disks-Latency": ['Block size', 'IO type', 'WR/RD', 'Jobs', 'Queue Depth', 'Lantency(us)']},
    "rand_write": {"Disks-IOPS": ['Block size', 'IO type', 'WR/RD', 'Jobs', 'Queue Depth', 'IOPS'],
                   "Disks-Latency": ['Block size', 'IO type', 'WR/RD', 'Jobs', 'Queue Depth', 'Lantency(us)']},
    # IOPS: ['read', 'write']
    "rand_mix": {"Disks-IOPS": ['Block size', 'IO type', 'Queue Depth', 'read', 'write'],
                 # Latency: ['read', 'write']
                 "Disks-Latency": ['Block size', 'IO type', 'Queue Depth', 'read', 'write']}
}

MIX_KEY_MAP = {
    "read": {"seq_mix": {"Disks-Bandwidth": 'Bandwidth(kB/s)', "Disks-Latency": 'Lantency(us)'},
             "rand_mix": {"Disks-IOPS": 'IOPS', "Disks-Latency": 'Lantency(us)'}},
    "write": {"seq_mix": {"Disks-Bandwidth": 'Bandwidth(kB/s).1', "Disks-Latency": 'Lantency(us).1'},
              "rand_mix": {"Disks-IOPS": 'IOPS.1', "Disks-Latency": 'Lantency(us).1'}}
}


def arg_parse():
    parser = argparse.ArgumentParser()
    # edit more out params here
    parser.add_argument('-d', '--device', dest='dev', default='all',
                        help='Target checking device, such as /dev/sfd0n1, "all" for all devices')
    parser.add_argument('-l', '--log-dir', dest='log_dir', required=True,
                        help="Test data directory")
    parser.add_argument('-o', '--output', dest="output", default='excel_output', help="logs output folder")
    return parser.parse_args()


def log_pre_handling(test_data_path):
    """
    csv log format: sfd2n1_seq_read_data_op.csv
    a) search and collect all matched data files: .csv, .log ...
    b) check data integrity of each file
    :param : test_data_path
    :return:
    """
    data_log_dir = {}
    for root, dir_name, files in os.walk(test_data_path):
        for file in files:
            if file.endswith('.csv'):
                logger.info("Found csv log: " + file)
                dev_name = str(file.split('_')[0])
                if dev_name.startswith("sfd") and dev_name not in data_log_dir.keys():
                    data_log_dir[dev_name] = []

                data_log_dir[dev_name].append(os.path.join(root, file))

    return data_log_dir


class DataParser:
    """
    a) extract data based on fields
    b) filter out usable data fields
    """
    def __init__(self, dev_name):
        self.dev = dev_name
        self.data_pool = {}

    @staticmethod
    def _check_data_integrity(item_name, ck_dict, primary_key='Block size'):
        """
        :param ck_dict:
        :param primary_key:
        :return:
        """
        len_primary = len(ck_dict[primary_key])
        if len_primary == 0:
            raise ValueError("{} length of {} is 0".format(item_name, primary_key))

        for key, value in ck_dict.items():

            if not value:
                raise ValueError("{}, {}: no data recorded".format(item_name, key))

            if len(value) != len_primary:
                raise ValueError("{} length of {} is not equal to length of {}".format(item_name, key, primary_key))

        logger.info("Checking data integrity of {}: Pass\n".format(item_name))
        return True

    def _parse_csv_data(self, theme, log_path, filed_list):
        fd_dict = {}
        raw_data = pd.read_csv(log_path)
        data_columns = raw_data.columns
        logger.debug("Data header-2:\n%s", raw_data.head(2))

        for item in filed_list:
            fd_dict[item] = list(raw_data[item]) if item in data_columns else None

        return fd_dict if self._check_data_integrity(theme, fd_dict) else None

    def read_data(self, key, log_dir):
        parse_rtn = None
        tar_fields = DATA_FIELDS_MAP.get(key)
        if not tar_fields:
            raise KeyError("{} is not a valid key in {}".format(key, DATA_FIELDS_MAP.keys()))

        if log_dir.endswith('.csv'):
            parse_rtn = self._parse_csv_data(key, log_dir, tar_fields)
        else:
            pass  # This left for other types log

        self.data_pool[key] = parse_rtn


class PyExl:
    def __init__(self, file_name):
        self.name = file_name
        self.writer = pd.ExcelWriter(file_name)

    @staticmethod
    def _check_fields_data_integrity(ck_fields, field_dev_data):
        for field in ck_fields:
            try:
                data_frame = pd.DataFrame(field_dev_data[field])
                data_columns = data_frame.columns
                data_frame_0 = data_frame[data_columns[0]]

                unmatched = [item for item in data_columns[1:] if 'False' in list(data_frame_0 == data_frame[item])]
                if unmatched:
                    raise ValueError("{}: data in {} is not matched with {}".
                                     format(field, str(unmatched), data_columns[0]))
            except RuntimeError:
                raise
        return True

    @staticmethod
    def _sort_dev_all(dev_list):
        dev_ptn = re.compile("sfdv?(?P<num>\d+)n\d+")  # sfdv0n1 is vanda device
        num_dev_map = {dev_ptn.search(dev).group('num'): dev for dev in dev_list if dev_ptn.search(dev)}

        sorted_dev_num = sorted([int(num) for num in num_dev_map.keys()])
        return [num_dev_map[str(num)] for num in sorted_dev_num]

    def create_data_frame(self, io_type, dev_field_dict):
        """
        :param io_type:
        :param dev_field_dict: {'dev1': {'Block size': [], 'xx': []}, 'seq_write': {}, ...}, 'dev2': {}}
        :return:
        """
        if io_type not in EXL_PARAM_MAP.keys():
            raise KeyError("{} not defined in {}".format(io_type, EXL_PARAM_MAP.keys()))
        else:
            logger.info("Cleaning data for " + io_type + " ...")

        dev_all = dev_field_dict.keys()
        sorted_dev_all = self._sort_dev_all(dev_all)
        frame_dict = {}

        for data_type, data_fields in EXL_PARAM_MAP[io_type].items():
            # format {"field_1": {"dev1": data_list, "dev2": data_list, ...}, "field_2": {}, ...}
            field_dev_dict = {}

            for field in data_fields:
                field = MIX_KEY_MAP[field][io_type][data_type] if field in MIX_KEY_MAP.keys() else field
                field_dev_dict.update({field: {dev: dev_field_dict[dev][field] for dev in dev_field_dict}})

            if io_type.endswith('mix'):
                check_same_fields = data_fields[:-2]  # except [read, write]
                ext_fields = data_fields[-2:]
            else:
                check_same_fields = data_fields[:-1]
                ext_fields = data_fields[-1:]

            if self._check_fields_data_integrity(check_same_fields, field_dev_dict):
                o_dic1, o_dic2, o_dic3 = OrderedDict(), OrderedDict(), OrderedDict()

                for field in check_same_fields:
                    dev_data_dict = field_dev_dict[field]
                    o_dic1[field] = dev_data_dict[sorted_dev_all[0]]

                for dev in sorted_dev_all:
                    for fd in ext_fields:
                        key = "{}-{}".format(fd, dev) if fd in MIX_KEY_MAP.keys() else dev
                        ext_fd = MIX_KEY_MAP[fd][io_type][data_type] if fd in MIX_KEY_MAP.keys() else fd
                        o_dic2[key] = field_dev_dict[ext_fd][dev]

                df1, df2 = pd.DataFrame(o_dic1), pd.DataFrame(o_dic2)
                # Mix need to be excepted
                df2_t = df2.T
                o_dic3['min'] = list(df2_t.min())
                o_dic3['max'] = list(df2_t.max())
                o_dic3['mean'] = list(df2_t.mean())

                frame_dict[data_type] = pd.concat([df1, df2,], axis=1)  # axis=1 connect x-axis, 0 y-axis
        return frame_dict

    def load_data(self, sheet_name, data_frame):
        data_frame.to_excel(self.writer, index=False, sheet_name=sheet_name)

    def multi_seq_perf_template(self):
        """
        Block size	IO type	WR/RD	Jobs	Queue Depth
        :return:
        """
        pass

    def save(self):
        self.writer.save()


if __name__ == '__main__':
    params = arg_parse()
    devices = params.dev
    log_dir = params.log_dir
    output = params.output

    if not os.path.exists(output):
        os.mkdir(output)

    if not os.path.exists(log_dir):
        raise ValueError("Test data directory not found: " + log_dir)

    csv_log_dict = log_pre_handling(log_dir)
    dev_data_pool = {}

    for dev, log_list in csv_log_dict.items():
        data_parser = DataParser(dev)
        for log in log_list:
            logger.info("Parsing log: " + log)
            [data_parser.read_data(item, log) for item in DATA_FIELDS_MAP.keys() if item in log]

        dev_data_pool[dev] = data_parser.data_pool

    # dev_data_pool: {'dev1': {'seq_read': {'Block size': [], 'xx': []}, 'seq_write': {}, ...},
    #                 'dev2': {'seq_read': {}, 'seq_write': {}, ...},
    #                 ...}
    # print(dev_data_pool['sfd7n1']['seq_read']['Bandwidth(kB/s)'])
    io_types = set([item for dev in dev_data_pool.keys() for item in dev_data_pool[dev].keys()])
    logger.info("All IO Types: " + str(io_types))

    for io_type in io_types:
        filename = "multi_disk_{}_perf.xlsx".format(io_type)  # Define excel file name
        file_dir = os.path.join(output, filename)
        exl = PyExl(file_dir)

        # {'dev1': {'Block size': [], 'xx': []}, 'seq_write': {}, ...}, 'dev2': {}}
        dev_field_data = {dev: dev_data_pool[dev][io_type] for dev in dev_data_pool.keys()}
        data_frame_dict = exl.create_data_frame(io_type, dev_field_data)

        for data_type, data_frame in data_frame_dict.items():
            exl.load_data(data_type, data_frame)

        exl.save()  # Very important, or no file created

        if os.path.exists(file_dir):
            logger.info("File %s created successfully", file_dir)
        else:
            logger.info("Create file %s failed", file_dir)

