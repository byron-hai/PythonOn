from socket import *
from threading import Thread


class Sender(Thread):
    def __init__(self, soc, dest):
        super().__init__()
        self.socket = soc
        self.dest_addr = dest

    def run(self):
        while self.socket:
            send_data = input("Please type in sending text:\n")
            self.socket.sendto(send_data.encode('utf-8'), dest_addr)
            if 'close' in send_data:
                break



class Recver(Thread):
    def __init__(self, soc, port):
        super().__init__()
        self.socket = soc
        self.port = port

    def run(self):
        udp_soc.bind(("", self.port))
        while self.socket:
            recv_data = udp_soc.recvfrom(1024)
            msg, from_addr = recv_data
            msg = msg.decode('utf-8')
            
            if 'close' in msg:
                print(f"{'=' * 32}\nConnection closed. Bye-Bye\n{'='*32}\n")
                break
            
            print("\nReceive from " + str(from_addr) + ": " + msg)
        

if __name__ == "__main__":
    dest_addr = ('127.0.0.1', 8080)
    udp_soc = socket(AF_INET, SOCK_DGRAM)
    td_recver = Recver(udp_soc, dest_addr[1])
    td_sender = Sender(udp_soc, dest_addr)

    print('=' * 32 + "\nSend 'close' for disconnection\n" + '=' * 32 + '\n')
    td_recver.start()
    td_sender.start()
    td_recver.join()
    td_sender.join()
    udp_soc.close()

