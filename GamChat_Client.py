# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 14:35:39 2021

@author: frechettem1
"""

import socket
import sys
from threading import Thread

host = '10.0.0.9'
port = 5000
name = input('Enter your name: ')
server = socket.socket()
server.connect((host, port))
    

def send_msg():
    while True:
        message = input('> ')
        server.send(('From ').encode() + name.encode() + (': ').encode() + str.encode(message))

def recv_msg():
    while True:
        data = server.recv(2048).decode()
        if not data:
            sys.exit(0)
        print(data)
        
Thread(target=recv_msg).start()
send_msg()

