from socket import *

cli_socket = socket(AF_INET, SOCK_STREAM)
dest_addr = ("127.0.0.1", 8080)
cli_socket.connect(dest_addr)

while 1:

    data_send = input("Data send: ")
    cli_socket.send(data_send.encode('utf-8'))
    if 'close' in data_send:
        break

    data_recv = cli_socket.recv(1024)
    print(data_recv.decode('utf-8'))

cli_socket.close()
