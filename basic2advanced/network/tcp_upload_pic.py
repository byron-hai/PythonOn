from socket import *
import os
import base64

cli_socket = socket(AF_INET, SOCK_STREAM)
dest_addr = ("127.0.0.1", 8080)
cli_socket.connect(dest_addr)

filepath = input("File for uploading: ")
if os.path.exists(filepath):
    with open(filepath, 'rb') as fr:
        data = fr.read()

    encoded_pic = base64.b64encode(data)
    cli_socket.send(encoded_pic)
    cli_socket.close()
