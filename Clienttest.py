import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('127.0.0.2', 8089))
msg = 'meu ovo'
clientsocket.send(msg.encode('utf-8'))

tabuleiro = ['-', '-', '-', '-', '-', '-', '-', '-', '-']