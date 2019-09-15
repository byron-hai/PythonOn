#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@ Desc: This script is used to transform data of iostat into visual chat(s). Besides, it can support
        comparison between devices, different logs or iostat fields. What's more, the up or down
        variation rate will be print out.

        Here're some examples:

        Scen1: one device and one iostat log file of this device
        ./iostat_data2chart.py -l iostat-log-path  # Default dev is /dev/sfd0n1

        Scen2: one device, but multiple iostat log files of this device
        # Here the first log will be set as reference log. Other log's data will be compared with this log's
        ./iostat_data2chart.py -l iostat-log-phase1-path,iostat-log-phase2-path

        Scen3: multi-devices and one iostat log file with data of theses devices recorded
        ./iostat_data2chart.py -d "/dev/dev-1,/dev/dev-2" -l iostat-log-path

        Scen4: multi-devices and multiple iostat log files with data of theses devices recorded
        # Here the first log will be set as reference log. Other log's data will be compared with this log's
        ./iostat_data2chart.py -d "/dev/dev-1,/dev/dev-2" -l iostat-log-phase1-path,iostat-log-phase2-path

        Scen5: abandon some start or/and end sample data
        ./iostat_data2chart.py -l iostat-log-path -f -s 100 -e 100

        Scen6: Assign iostat fields(Default is rMB/s,wMB/s)
        ./iostat_data2chart.py -l iostat-log-path -f "r/s,w/s"

        Scen7: Give an specific title to chart. (Default a title still be given)
        ./iostat_data2chart.py -l iostat-log-path -t "This is different title"

        Note: Necessary tool/lib such as python3, numpy, matplotlib need to be
              installed before run this script

@ author: byron
@ Date: 2019-08-06
@ History: 2019-0806 Version 1.0
"""

import argparse
import os
import logging
import subprocess as sp
import random
import numpy as np
import matplotlib.pylab as plt


DATE_FMT = '%y%m%d %H:%M:%S'
LOG_FMT = "%(asctime)s %(filename)s %(levelname)s: %(message)s"
logging.basicConfig(level=logging.INFO, format=LOG_FMT, datefmt=DATE_FMT)
logger = logging.getLogger("iostat_viewer")

'''
r/s            Read operation number per second
w/s'           Write operation number per second
rMB/s, rkB/s'  Read MB/KB per second
wMB/s, wkB/s   Write MB/KB per second
await          Average wait time (milliseconds)
r_await        Average read action duration
w_await        Average write action duration
%util          IO / CPU
'''

IOSTAT_FIELDS = ['r/s', 'w/s', 'rMB/s', 'rkB/s', 'wMB/s', 'wkB/s', 'await', 'r_await', 'w_await', '%util']
# Did not found a better way to gen random color
COLOR_LIB = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#00FFFF',
             '#556B2F', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
             '#9370DB', '#191970', '#008B8B', '#D2691E', '#A9A9A9', '#00BFFF']


def arg_parse():
    parser = argparse.ArgumentParser()
    # edit more out params here
    parser.add_argument('-d', '--device', dest='dev', default='/dev/sfd0n1',
                        help='Target checking device, such as /dev/sfd0n1, "all" for all devices')
    parser.add_argument('-f', '--fields', dest='iostat_fd', default='rMB/s,wMB/s',
                        help='iostat fields(Separate with comma for multi-items), sunch as rMB/s, rkB/s '
                             'wMB/s, wkB/s, await, r_await, w_await, util')
    parser.add_argument('-l', '--log-file', dest='iostat_log', required=True,
                        help="iostat log file(s). Separate with comma if more files")
    parser.add_argument('-s', '--start-offset', dest="start_offset", default=60, type=int,
                        help="Start offset number from start")
    parser.add_argument('-e', '--end-offset', dest="end_offset", default=60, type=int,
                        help="End offset number from end")
    parser.add_argument('-t', '--title', dest="title", help="Chart title")
    parser.add_argument('-r', '--range', dest="range", type=int, default=0,
                        help="Updown range percentage, such as 10 for 10%")
    parser.add_argument('-o', '--output', dest="output", default=os.getcwd(), help="logs output folder")
    return parser.parse_args()


def check_logs(log_list, field_list, dev_list):
    """ check log, fields """
    for log in log_list:
        logger.info("Checking log files")
        if not os.path.exists(log):
            raise RuntimeError("Log files not found: {}".format(log))

        log_fields = sp.getoutput("cat {} | grep 'Device:' | head -n 1".format(log))
        ck_fields = [fd for fd in field_list if fd not in log_fields]
        if ck_fields:
            raise RuntimeError("Fields: {} not found in log file {}".format(ck_fields, log))

        for dev in dev_list:
            dev = os.path.basename(dev)
            if dev not in sp.getoutput("cat {} | grep {}".format(log, dev)):
                raise RuntimeError("Device {} has no data recorded in log {}".format(dev, log))
        logger.info("Checking passed: " + log)


def parse_iostat_log(log_file, dev_name, field):
    """ extract data from log """
    fields = sp.getoutput("cat {} | grep 'Device:' | head -n 1".format(log_file))
    index = fields.split().index(field)
    logger.debug("Extract data: {fd} of {dev} from {log}".format(fd=field, dev=dev_name, log=log_file))
    with open(log_file, 'rt') as fr:
        lines = fr.readlines()

    return [float(line.split()[index]) for line in lines if line.startswith(dev_name)]


class Chart:
    def __init__(self, title, x_label=None, y_label=None, output=None):
        self.title = title
        self.xlabel = x_label if x_label else 'Sample number'
        self.ylabel = y_label if y_label else 'Axis-Y'
        self.legent_font_size = 'medium'  # [‘xx-small’, ‘x-small’, ‘small’, ‘medium’, ‘large’, ‘x-large’, ‘xx-large’]
        self.output = output

        if output and not os.path.exists(output):
            os.makedirs(output)
        else:
            self.output = os.getcwd()

    def single_dev_iostat_draw(self, field_val_dict, start_offset=0, end_offset=0, vari_range=0):
        """
        :param field_val_dict:
        :param start_offset:
        :param end_offset:
        :return:
        """
        sub_fig_num = len(field_val_dict.keys())
        fig = plt.figure(figsize=(12, 4 * sub_fig_num), dpi=200)
        index = 1

        for item, val_list in field_val_dict.items():
            size = len(val_list)
            if size == 0:
                logger.warning("{}: {}, List is Empty. Skipped".format(item, val_list))
                continue

            sample_size = len(val_list)
            if start_offset + end_offset > sample_size:
                raise OverflowError("Got no data after remove offset items. Please set offset smaller")

            plt.subplot(sub_fig_num, 1, index)
            plt.title(self.title) if index == 1 else None
            plt.ylabel(item)
            x_size = sample_size - (start_offset + end_offset)
            x_val = np.arange(1, x_size + 1)

            color_id = random.randint(0, len(COLOR_LIB) - 2)
            y_val = np.array(val_list[start_offset: x_size + start_offset])
            y_mean = np.mean(y_val)
            y_mean_val = 0 * x_val + y_mean
            y_up = 0 * x_val + y_mean * (1 + vari_range / 100)
            y_down = 0 * x_val + y_mean * (1 - vari_range / 100)
            plt.axis([0, x_size, 0, np.max(y_val) * 1.1])
            plt.plot(x_val, y_val, color=COLOR_LIB[color_id], linewidth=1.0, label=item)
            plt.plot(x_val, y_mean_val, color=COLOR_LIB[color_id + 1], linestyle=':', linewidth=1.5,
                     label='Mean-{}:{:.2f}'.format(item, y_mean))
            plt.plot(x_val, y_up, color=COLOR_LIB[color_id + 1], linestyle='-.', linewidth=1.5,
                     label='{}% Up'.format(vari_range))
            plt.plot(x_val, y_down, color=COLOR_LIB[color_id + 1], linestyle='-.', linewidth=1.5,
                     label='{}% Down'.format(vari_range))
            plt.legend(loc="best", fontsize=self.legent_font_size, frameon=False)
            index += 1

        fig_dir = os.path.join(self.output, "-".join(self.title.split()) + ".png")
        fig.savefig(fig_dir)
        logger.info("Drawing over. Check at %s", fig_dir)
        return

    def single_dev_iostat_comp_draw(self, field_log_dict, start_offset=0, end_offset=0):
        """
        :param field_log_dict: {'Field-A': {'log-a': val_list, 'log-b': val_list},
                                'Field-B': {'log-a': val_list, 'log-b': val_list},
                                ...}
        :param start_offset:
        :param end_offset:
        :return:
        """
        sample_size_dict = dict()
        for fd, log_val_dict in field_log_dict.items():
            sample_size = min([len(val_lst) for val_lst in log_val_dict.values()])
            if sample_size == 0:
                logger.warning("The minimum sample size of {} is 0. Please check log-file".format(fd))
            else:
                sample_size_dict.update({fd: sample_size})

        sub_fig_num = len(sample_size_dict.keys())
        fig = plt.figure(figsize=(12, 6 * sub_fig_num), dpi=200)
        index, color_index = 1, 0

        for fd, sample_size in sample_size_dict.items():
            sample_size = sample_size
            if start_offset + end_offset > sample_size:
                raise OverflowError("Got no data after remove offset items. Please set offset smaller")

            plt.subplot(sub_fig_num, 1, index)
            plt.title(self.title) if index == 1 else None
            plt.ylabel(fd)
            x_size = sample_size - (start_offset + end_offset)
            x_val = np.arange(0, x_size)
            index_log, y_mean_ref = 1, 0

            for log, val_list in field_log_dict[fd].items():
                y_val = np.array(val_list[start_offset: x_size + start_offset])

                if index_log == 1:
                    y_mean_ref = y_mean = np.mean(y_val)
                else:
                    y_mean = np.mean(y_val)

                y_mean_vari = (y_mean - y_mean_ref) * 100 / y_mean_ref
                y_mean_val = 0 * x_val + y_mean
                plt.axis([0, x_size, 0, np.max(y_val) * 1.1])

                plt.plot(x_val, y_val, color=COLOR_LIB[color_index], linewidth=1.0, label=log + ':' + fd)
                plt.plot(x_val, y_mean_val, color=COLOR_LIB[color_index + 1], linestyle=':', linewidth=1.5,
                         label='{}: Mean-{}:{:.2f}'.format(log, fd, y_mean) if index_log == 1 else
                         '{}: Mean-{}:{:.2f} ({:.2f}%)'.format(log, fd, y_mean, y_mean_vari))
                index_log += 1
                color_index += 1

            plt.legend(loc="best", fontsize=self.legent_font_size, frameon=False)
            index += 1
            color_index += 1

        fig_dir = os.path.join(self.output, "-".join(self.title.split()) + ".png")
        fig.savefig(fig_dir)
        logger.info("Drawing over. Check at %s", fig_dir)
        return

    def multi_dev_iostat_draw(self, field_dev_dict, start_offset=0, end_offset=0):
        """
        :param field_dev_dic: {'Field-A': {'dev-a': val_list, 'log-b': val_list},
                               'Field-B': {'dev-b': val_list, 'log-b': val_list},
                               ...}
        :param start_offset:
        :param end_offset:
        :return:
        """
        sample_size_dict = dict()
        for fd, dev_val_dict in field_dev_dict.items():
            sample_size = min([len(val_lst) for val_lst in dev_val_dict.values()])
            if sample_size == 0:
                logger.warning("The minimum sample size of {} is 0. Please check log-file".format(fd))
            else:
                sample_size_dict.update({fd: sample_size})

        sub_fig_num = len(sample_size_dict.keys())
        fig = plt.figure(figsize=(12, 6 * sub_fig_num), dpi=200)
        index = 1

        for fd, sample_size in sample_size_dict.items():
            sample_size = sample_size
            if start_offset + end_offset > sample_size:
                raise OverflowError("Got no data after remove offset items. Please set offset smaller")

            plt.subplot(sub_fig_num, 1, index)
            plt.title(self.title) if index == 1 else None
            plt.ylabel(fd)
            x_size = sample_size - (start_offset + end_offset)
            x_val = np.arange(0, x_size)

            for dev, val_list in field_dev_dict[fd].items():
                color_id = random.randint(0, len(COLOR_LIB) - index)
                y_val = np.array(val_list[start_offset: x_size + start_offset])
                y_mean = np.mean(y_val)
                y_mean_val = 0 * x_val + y_mean
                plt.axis([0, x_size, 0, np.max(y_val)])
                plt.plot(x_val, y_val, color=COLOR_LIB[color_id], linewidth=1.0, label=dev + ':' + fd)
                plt.plot(x_val, y_mean_val, color=COLOR_LIB[color_id + 1], linestyle=':', linewidth=1.5,
                         label='{}: Mean-{}:{:.2f}'.format(dev, fd, y_mean))

            plt.legend(loc="best", fontsize=self.legent_font_size, frameon=False)
            index += 1

        fig_dir = os.path.join(self.output, "-".join(self.title.split()) + ".png")
        fig.savefig(fig_dir)
        logger.info("Drawing over. Check at %s", fig_dir)
        return


if __name__ == '__main__':
    """ Main """

    params = arg_parse()
    devices = params.dev
    data_fields = params.iostat_fd
    iostat_logs = params.iostat_log
    start_offset = params.start_offset
    end_offset = params.end_offset
    title = params.title
    vari_range = params.range
    output = params.output

    dev_list = [dev.strip() for dev in devices.split(',')]
    log_list = [log.strip() for log in iostat_logs.split(',')]
    field_list = [field.strip() for field in data_fields.split(',')]

    undefined_fd = [item for item in field_list if item not in IOSTAT_FIELDS]
    if undefined_fd:
        raise ValueError("{} not defined in IOSTAT_FIELDS".format(undefined_fd))

    check_logs(log_list, field_list, dev_list)
    dev_num, log_num = len(dev_list), len(log_list)

    if dev_num == 1 and log_num == 1:
        log, dev = log_list[0], dev_list[0]
        dev_name = os.path.basename(dev)
        dev_fd_dict = {fd: parse_iostat_log(log, dev_name, fd) for fd in field_list}
        title = title if title else "{} iostat chart".format(dev_name)
        figure = Chart(title, output=output)
        figure.single_dev_iostat_draw(dev_fd_dict, start_offset=start_offset,
                                      end_offset=end_offset, vari_range=vari_range)

    elif dev_num == 1 and log_num > 1:
        dev = dev_list[0]
        dev_name = os.path.basename(dev)
        fd_log_dict = dict()

        for fd in field_list:
            log_fd_dict = {os.path.basename(log): parse_iostat_log(log, dev_name, fd) for log in log_list}
            fd_log_dict.update({fd: log_fd_dict})

        title = title if title else "{} iostat comparison chart".format(dev_name)
        figure = Chart(title, output=output)
        figure.single_dev_iostat_comp_draw(fd_log_dict, start_offset=start_offset, end_offset=end_offset)

    elif dev_num > 1 and log_num == 1:
        log = log_list[0]
        fd_dev_dict = dict()

        for fd in field_list:
            dev_fd_dict = {os.path.basename(dev): parse_iostat_log(log, dev, fd) for dev in dev_list}
            fd_dev_dict.update({fd: dev_fd_dict})

        title = title if title else "multi-dev iostat chart"
        figure = Chart(title, output=output)
        figure.multi_dev_iostat_draw(fd_dev_dict, start_offset=start_offset, end_offset=end_offset)

    elif dev_num > 1 and log_num > 1:
        for dev in dev_list:
            dev_name = os.path.basename(dev)
            fd_log_dict = dict()

            for fd in field_list:
                log_fd_dict = {os.path.basename(log): parse_iostat_log(log, dev_name, fd) for log in log_list}
                fd_log_dict.update({fd: log_fd_dict})
            title = "{}-{}".format(dev_name, title) if title else "{} iostat comparison chart".format(dev_name)
            figure = Chart(title, output=output)
            figure.single_dev_iostat_comp_draw(fd_log_dict, start_offset=start_offset, end_offset=end_offset)
    else:
        raise RuntimeError("Device number or log file number is 0")
