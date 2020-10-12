from socket import *

tcp_socket = socket(AF_INET, SOCK_STREAM)
dest_addr = ("127.0.0.1", 8080)

tcp_socket.connect(dest_addr)

data_send = "Hello world"

tcp_socket.send(data_send.encode('utf-8'))
data_recv = tcp_socket.recv(1024)
print(data_recv.decode('utf-8'))
tcp_socket.close()
