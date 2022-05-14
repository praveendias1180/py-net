from audioop import add
import socket
port = 1234
address = "127.0.0.1"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((address, port))
server.listen(7)
print("RQ server listening...")

while True:
    con, addr = server.accept()
    print("Connection address is ", addr)
    con.send(bytes("Hello, Welcome to RQ server!", "utf-8"))