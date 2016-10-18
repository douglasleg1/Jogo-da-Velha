import socket

tabuleiro = ['-', '-', '-', '-', '-', '-', '-', '-', '-']

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('127.0.0.2', 8089))
serversocket.listen(5) # become a server socket, maximum 5 connections

while True:
    print('Aguardando')
    connection, address = serversocket.accept()
    msg = connection.recv(64)
    if len(msg) > 0:
        print (msg.decode('utf-8'))
        break