import socket
import random

a = random.randint(1, 26)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 100))
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

print(a)