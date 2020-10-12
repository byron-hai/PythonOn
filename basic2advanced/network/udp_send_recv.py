from socket import *

dest_addr = ('127.0.0.1', 8080)
udp_soc = socket(AF_INET, SOCK_DGRAM)
udp_soc.bind(("", 8080))

send_data = input("Input send data:\n")
udp_soc.sendto(send_data.encode('utf-8'), dest_addr)

recv_data = udp_soc.recvfrom(1024)
msg, from_addr = recv_data
print(str(from_addr) + ": " + msg.decode("utf-8"))
udp_soc.close()





