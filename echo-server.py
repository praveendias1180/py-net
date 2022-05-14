from audioop import add
import socket
port = 1235
address = "127.0.0.1"
BUF_SIZE = 3

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((address, port))
server.listen(7)
print("RQ server listening...")

while True:
    con, addr = server.accept()
    print("Connection address is ", addr)

    data = con.recv(BUF_SIZE)
    print(data.decode("utf-8"))
    con.send(data)