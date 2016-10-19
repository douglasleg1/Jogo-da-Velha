import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 8089
clientsocket.connect((host,port))
print('Conectado a',host)

while True:
    print('Esperando resposta...')
    recebido = clientsocket.recv(1024)
    print ('\n'+host+' enviou:\n'+recebido.decode('utf-8')+'\n')
    msg = input('Cliente, envie a mensagem para o servidor: ')
    clientsocket.send(msg.encode('utf-8'))
    print('Mensagem enviada')
