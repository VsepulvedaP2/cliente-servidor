import socket
import os
import subprocess


class Client:
    def __init__(self):
        self.s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        self.host = "localhost"
        self.port = 10001
        self.address = (self.host, self.port)
        self.initial = True

    def connect(self):
        while self.initial:
            try:
                print("conecting...")
                self.s.connect(self.address)
                self.initial = False
            except socket.error as e:
                print(e)
        print("connected")

    def run(self):
        self.connect()


if __name__ == "__main__":
    cliente = Client()
    cliente.run()
