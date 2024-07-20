#Using file interface in Python which wraps an underlying interface
import socket 

HOST = '0.0.0.0'
PORT = 8080
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind((HOST, PORT))
message, addr = udp_socket.recvfrom(1024)
udp_socket.sendto(message.upper(), addr)
