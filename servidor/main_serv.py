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

    def connect(self):
        # while True:
        print("waiting for connection..")
        sleep(1)
        self.s.bind(self.address)
        self.s.listen(1)
        self.socket_client, self.addr = self.s.accept()
        print("connected")

    def run(self):
        self.connect()


if __name__ == "__main__":
    servidor = Server()
    servidor.run()
