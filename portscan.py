import socket
p = input("ポート番号")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), p))
s.listen(5)

while True:
    clientsocket, addr = s.accept()
    print(f"Connection from {addr} has been established!")
    clientsocket.close()