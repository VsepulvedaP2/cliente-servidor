import socket
import sys
import chardet
import os
from time import sleep


class Server:
    def __init__(self):
        self.s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        self.host = "localhost"
        self.port = 10001
        self.address = (self.host, self.port)
        self.key = "pass"

    def connect(self):
        # while True:
        print("waiting for connection..")
        sleep(1)
        self.s.bind(self.address)
        self.s.listen(1)
        self.client_socket, self.addr = self.s.accept()
        print("connected")

    def run(self):
        self.connect()
        self.authentication()

    def authentication(self):
        self.door = False
        while not self.door:
            try:
                print("authentication..")
                request = self.client_socket.recv(8192).decode()
                print(request)
            except socket.error as msg:
                print(msg)
            if request == self.key:
                print(request)
                print("finalized authentication")
                self.client_socket.sendall("open".encode('utf-8'))
                self.door = True


if __name__ == "__main__":
    servidor = Server()
    servidor.run()
