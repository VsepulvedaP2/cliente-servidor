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
        self.key = "pass"

    def connect(self):
        while self.initial:
            try:
                print("conecting...")
                self.s.connect(self.address)
                self.initial = False
            except socket.error as e:
                print(e)
        print("connected")

    def authentication(self):
        print("authentication..")
        self.s.sendall(self.key.encode())
        self.firstAnswer = self.s.recv(8192).decode()
        print(self.firstAnswer)

    def run(self):
        self.connect()
        self.authentication()
        self.handler(self.firstAnswer)

    def handler(self, door):
        if door == "open":
            self.door = True
        else:
            print("no access")
        while self.door:
            print("test door")
            break


if __name__ == "__main__":
    cliente = Client()
    cliente.run()
