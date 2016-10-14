from socket import *
host = '192.168.0.105'
port = 5000
tcp = socket(AF_INET, SOCK_STREAM)
dest = (host, port)
matriz1=[[0,0,0,0,0,0,1,0,0,0], [0,0,0,0,0,0,1,0,0,0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0,0,0,0,0,0,1,0,0,0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

tcp.bind(dest)
tcp.listen(1)


def verifica_tiro_entrada(x,y):
    if matriz1[x][y] == 1:
        conexao.send(b'#')
    else:
        conexao.send(b'*')
def verifica_tiro_saida (x, y, algo):
    matriz1[x][y] = algo        
        
        
while True:
    conexao, cliente = tcp.accept()
    while True:
        print('aguardando o usuario online atirar...\nwait please')
        for i in range(2):
            if i ==0:
                x = conexao.recv(1024)
                x = str(x,'utf-8')
                x = int(x)                
            else:
                y = conexao.recv(1024)
                y = str(y, 'utf-8')
                y = int(y)        
        
        verifica_tiro_entrada(x-1,y-1)
        for j in range(2):
            if j ==0:
                while True:
                    try:
                        x_local = int(input('x: '))
                        adversario_x = x_local
                        if x_local<0 or x_local>10:
                            print('invalido')
                            continue
                        else:
                            break
                    except:
                        continue
                x_local = bytes(str(x_local),'utf-8')
                conexao.send(x_local)
                        
            else:
                while True:
                    try:
                        y_local = int(input('y: '))
                        adversario_y = y_local
                        if y_local<0 or y_local>10:
                            print('invalido')
                            continue
                        else:
                            break
                    except:
                        continue
                y_local = bytes(str(y_local), 'utf-8')
                conexao.send(y_local)
                teste_dado = conexao.recv(1024)
                teste_dado = str(teste_dado, 'utf-8')

        verifica_tiro_saida (adversario_x-1, adversario_y-1, teste_dado)
        for k in matriz1:
            print(k)
