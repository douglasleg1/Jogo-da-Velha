from socket import *
host = 'localhost'
port = 5000
tcp = socket(AF_INET, SOCK_STREAM)
dest = (host, port)
#conexao, cliente = tcp.accpet()
tcp.connect(dest)
def verifica_tiro_saida (x, y, algo_que_foi_recebedo_da_net):
    matriz[x][y] = algo_que_foi_recebedo_da_net
def verifica_tiro_entrada(x,y):
    if matriz[x][y] == 1:
        tcp.send(b'0')
    else:
        tcp.send(b'0')

matriz=[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

while True:
    for i in range(2):
        if i == 0:
            while True:
                try:
                    x =int(input('x: '))
                    x1 = x
                    if x<0 or x>10:
                        print('invalido')
                        continue
                    else:
                        break
                except:
                    print('invalido novamente')
                    continue
            x = bytes(str(x), 'utf-8')
            tcp.send(x)
        else:
            while True:
                try:
                    y =int(input('y: '))
                    y1 = y
                    if y<0 or y>10:
                        print('invalido')
                        continue
                    else:
                        break
                except:
                    print('invalido novamente')
                    continue
            y = bytes(str(y), 'utf-8')
            tcp.send(y)
            teste = tcp.recv(1024)
            teste = str(teste, 'utf-8')
            teste = int(teste)
    verifica_tiro_saida(x1-1,y1-1,teste)
    for i in matriz:
        print(i)
    print('aguardando o usuario online atirar...\n wait please')
    for j in range(2):
        if j==0:
            x_adversario = tcp.recv(1024)
            x_adversario = str(x_adversario, 'utf-8')
            x_adversario = int(x_adversario)
        else:
            y_adersario = tcp.recv(1024)
            y_adersario = str(y_adersario, 'utf-8')
            y_adersario = int(y_adersario)
    verifica_tiro_entrada(x_adversario-1,y_adersario-1)

tcp.close
