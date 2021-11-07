# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 16:51:58 2021

@author: soloveyg
"""

import socket

ClientSocket = socket.socket()
host = '10.220.50.195'
port = 5000

print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

Response = ClientSocket.recv(1024)

while True:
    Input = input('Say Something: ')
    ClientSocket.send(str.encode(Input))
    Response = ClientSocket.recv(1024)
    print(Response.decode('utf-8'))

ClientSocket.close()