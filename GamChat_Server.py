# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 14:17:11 2021

@author: frechettem1
"""

import socket
import os
#threading clients
from _thread import*

ServerSocket = socket.socket()
host = '10.0.0.9'
port = 5000

try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))
    
print('Waitiing for a Connection..')
# client limit is 100
ServerSocket.listen(100)

list_of_clients = []

def threadedClient(conn, address):
    conn.send(str.encode('Welcome to GamChat'))
    while True:
            try:
                message = conn.recv(2048)
                if message:
                    # Calls broadcast function to send message to all
                    message_to_send = message.decode()
                    broadcast(message_to_send)
                else:
                    removeConn(conn)
            except:
                continue
    
def broadcast(message):
     for client in list_of_clients:
         try:
             client.send(message.encode())
         except:
             client.close()
             removeConn(client)

#removes a user from list_of_clients without an error
def removeConn(conn):
    if conn in list_of_clients:
        list_of_clients.remove(conn)
    
while True:
    conn, addr = ServerSocket.accept()
    list_of_clients.append(conn)
    print (addr[0] + " connected")
    start_new_thread(threadedClient,(conn,addr))  
    
