from socket import *

tcp_socket = socket(AF_INET, SOCK_STREAM)
tcp_socket.bind(("", 8080))
tcp_socket.listen(10)
while 1:
    c, addr = tcp_socket.accept()
    msg = c.recv(1024)
    print(msg.decode('utf-8'))
    c.send("We connected!".encode('utf-8'))
tcp_socket.close()

