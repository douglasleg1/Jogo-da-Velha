import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 8089

serversocket.bind((host,port))

serversocket.listen(5) # become a server socket, maximum 5 connections
connection = None


while True:
    if connection == None:
        print('Aguardando conexão')
        connection, address = serversocket.accept()
        print ('Conectado com',address[0])
    else:
        enviado = input('Diga algo ao cliente: ')
        connection.send(enviado.encode('utf-8'))
        print('Mensagem Enviada')
        recebido = connection.recv(1024)
        print('\n'+str(address[0])+' enviou:\n'+recebido.decode('utf-8')+'\n')