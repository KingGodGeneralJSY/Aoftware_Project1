import sys, socket


IP = "127.0.0.1"
PORT = 8888
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 8888))

print("start listen")
s.listen(1)

csocket, address = s.accept()

print(address)
while True:
    date = csocket.recv(1024)
    print(date.decode())


s.close()