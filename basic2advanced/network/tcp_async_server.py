from socket import *
from threading import Thread


class Conn(Thread):
    def __init__(self, con, from_addr):
        super().__init__()
        self.con = con
        self.from_addr = str(from_addr)
        print(self.from_addr + " connected")

    def run(self):
        while 1:
            rtn = self.recv()
            if rtn == 'close':
                self.con.close()
                break

            self.send()
    
    def send(self):
        data = input("Type in sending message:\n").encode('utf-8')
        self.con.send(data)

    def recv(self):
        msg = self.con.recv(1024)
        msg = msg.decode('utf-8')

        if "close" in msg:
            print("Close connection with ", self.from_addr)
            return 'close'

        print(f"Receive from {self.from_addr}: ", msg)


if __name__ == "__main__":
    ser_socket = socket(AF_INET, SOCK_STREAM)
    ser_socket.bind(("", 8080))
    ser_socket.listen(10)

    while 1:
        con, addr = ser_socket.accept()
        Conn(con, addr).start()
    

