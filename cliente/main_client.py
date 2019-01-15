import socket
import os
import subprocess


class client:
    def __init__(self):
        self.s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        self.host = "localhost"
        self.port = 10001
        self.direccion_fuente = (self.host, self.port)

    def conect(self):
        while True:
