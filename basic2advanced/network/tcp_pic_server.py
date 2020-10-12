from socket import *
import base64
import os

tcp_socket = socket(AF_INET, SOCK_STREAM)
tcp_socket.bind(("", 8080))
tcp_socket.listen(10)
while 1:
    c, addr = tcp_socket.accept()
    print(str(addr) + " connected")
    byte_data = bytes()
    recv = c.recv(1024)
    while recv:
         byte_data += recv
         recv = c.recv(1024)

    load_pic = base64.b64decode(byte_data)
    pic_path = "pic/upload_pic.jpg"
    with open(pic_path, 'wb') as fw:
        fw.write(load_pic)

    if os.path.exists(pic_path):
        print("Uploading picture successful. check in ", pic_path)

c.close()
