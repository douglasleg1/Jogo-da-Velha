import time, socket

def imprime(tabuleiro):
    print("")
    print("\t\t      |     |     ")
    print("\t\t   %s  |  %s  |  %s " % (tabuleiro[6], tabuleiro[7], tabuleiro[8]))
    print("\t\t _____|_____|_____")
    print("\t\t      |     |     ")
    print("\t\t   %s  |  %s  |  %s " % (tabuleiro[3], tabuleiro[4], tabuleiro[5]))
    print("\t\t _____|_____|_____")
    print("\t\t      |     |     ")
    print("\t\t   %s  |  %s  |  %s " % (tabuleiro[0], tabuleiro[1], tabuleiro[2]))
    print("\t\t      |     |     ")
    print("")

def CondVitoria(tabuleiro):
    #checa linhas
    for i in range(3):
        if len(set(tabuleiro[i * 3:i * 3 + 3])) is 1 and tabuleiro[i * 3] is not '-': return True
    #checa colunas
    for i in range(3):
        if (tabuleiro[i] is tabuleiro[i + 3]) and (tabuleiro[i] is tabuleiro[i + 6]) and tabuleiro[i] is not '-':
            return True
    #checa diagonais
    if tabuleiro[0] is tabuleiro[4] and tabuleiro[4] is tabuleiro[8] and tabuleiro[4] is not '-':
        return True
    if tabuleiro[2] is tabuleiro[4] and tabuleiro[4] is tabuleiro[6] and tabuleiro[4] is not '-':
        return True
    return False

def proximaJogada(tabuleiro, player):
    if len(set(tabuleiro)) == 1: return 0, 4

    proximoJogador = 'X' if player == 'O' else 'O'
    if CondVitoria(tabuleiro):
        if player is 'X':
            return -1, -1
        else:
            return 1, -1
    res_list = []  # lista com os resultados
    c = tabuleiro.count('-')  # contador de espaços vazios
    if c is 0:
        return 0, -1
    _list = []  # list com as posições onde '-' aparece
    for i in range(len(tabuleiro)):
        if tabuleiro[i] == '-':
            _list.append(i)
    for i in _list:
        tabuleiro[i] = player
        ret, move = proximaJogada(tabuleiro, proximoJogador)
        res_list.append(ret)
        tabuleiro[i] = '-'
    if player is 'X':
        maxele = max(res_list)
        return maxele, _list[res_list.index(maxele)]
    else:
        minele = min(res_list)
        return minele, _list[res_list.index(minele)]

def PlayerVsAI(player,tabuleiro):

    imprime(tabuleiro)
    while True:
        proximo = proximaJogada(tabuleiro, player)
        if proximo[1] != -1:
            if player == 'O':
                proximo = proximaJogada(tabuleiro, player)
                print('Vez do computador')
                time.sleep(0.5)
                jogada = proximo[1] + 1

            else:
                while True:
                        while True:
                            try:
                                jogada = int(input('Jogador com o %s, digite a sua jogada:' %player))
                                break
                            except ValueError or IndexError:
                                print("Valor Inválido!")
                                continue

                        if jogada in range(10):
                            break
                        else:
                            print('Jogada inválida')
                            continue


            if tabuleiro[jogada - 1] == '-':
                tabuleiro[jogada - 1] = player
                print('\n')
                print ('\t\t\tJogada válida!')
                imprime(tabuleiro)

                vitoria = CondVitoria(tabuleiro)

                if vitoria == True:
                    if player == 'O':
                        print(' O computador ganhou, hehehe!\n')
                    else:
                        print(" Você ganhou! Parabéns!")
                    break

                if player == 'X':
                    player = 'O'

                else:
                    player = 'X'
            else:
                print('Jogada inválida, casa ocupada, tente novamente\n')
                continue
        else:
            print('\t\tDeu empate!!!\n')
            break

def PlayerVSPlayer(player,tabuleiro):
    imprime(tabuleiro)
    while True:
            while True:
                try:
                    jogada = int(input('Jogador com o %s, digite a sua jogada:' %player))
                    break
                except ValueError or IndexError:
                    print("Valor Inválido!")


            if tabuleiro[jogada - 1] == '-':
                tabuleiro[jogada - 1] = player
                imprime(tabuleiro)

            else:
                print('Jogada inválida, casa ocupada, tente novamente\n')
                continue

            vitoria = CondVitoria(tabuleiro)

            if vitoria == True:
                if player == 'O':
                    print("O jogador com o a 'O' ganhou!")
                else:
                    print("O jogador com o 'X' ganhou!")
                break

            if player == 'X':
                player = 'O'

            else:
                player = 'X'

            if tabuleiro.count('-') == 0 and vitoria == False:
                print('Deu empate!!!\n')
                break

def Client(player,tabuleiro):
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #host = socket.gethostname()
    def roda():
        while True:
            try:
                host = input("Digite a identificação do outro usuário: ")
                if host != '':
                    return host
                else:
                    print("Digite uma identicação válida!")
                    continue
            except OSError:
                print("Digite a identificação correta!")
                continue
    port = 8089
    while True:
        try:
            clientsocket.connect((roda(), port))
            break
        except socket.gaierror:
            continue
    print('Conectado a', host)
    imprime(tabuleiro)

    while True:

        if player == 'X':
            print('Vez do X')
            jogada = clientsocket.recv(1024)
            jogada = int(jogada.decode('utf-8'))
            tabuleiro[jogada - 1] = player
            print('\n')
            print('\t\t\tJogada válida!')
            imprime(tabuleiro)

            vitoria = CondVitoria(tabuleiro)

            if vitoria == True:
                print(player, 'ganhou, parabéns!\n')
                clientsocket.shutdown(socket.SHUT_RDWR)
                clientsocket.close()
                break

            if player == 'X':
                player = 'O'

            else:
                player = 'X'

        else:
            print('Vez do O')
            while True:
                try:
                    jogada = int(input('Jogador com o %s, digite a sua jogada:' % player))
                    break
                except ValueError or IndexError:
                    print("Valor Inválido!")
                    continue

            if tabuleiro[jogada - 1] == '-':
                clientsocket.send(str(jogada).encode('utf-8'))
                tabuleiro[jogada - 1] = player
                print('\n')
                print('\t\t\tJogada válida!')
                imprime(tabuleiro)
            else:
                print('Jogada inválida, casa ocupada, tente novamente\n')
                continue

            vitoria = CondVitoria(tabuleiro)

            if vitoria == True:
                if player == 'O':
                    print("O jogador com o 'O' ganhou!")
                else:
                    print("O jogador com o 'X' ganhou!")
                clientsocket.shutdown(socket.SHUT_RDWR)
                clientsocket.close()
                break

            if player == 'X':
                player = 'O'

            else:
                player = 'X'

            if tabuleiro.count('-') == 0 and vitoria == False:
                print('Deu empate!!!\n')
                break

def Server(player,tabuleiro):
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = ''
    port = 8089
    print("Divulgue para o seu adversário essa identificação: ",host)
    serversocket.bind((host, port))

    serversocket.listen(5)  # become a server socket, maximum 5 connections
    connection = None
    imprime(tabuleiro)

    while True:
        if connection == None:
            print('Aguardando conexão')
            connection, address = serversocket.accept()
            print('Conectado com', address[0])
        else:
            while True:
                if player == 'O':
                    print('Vez do O')
                    jogada = connection.recv(1024)
                    jogada = int(jogada.decode('utf-8'))
                    tabuleiro[jogada - 1] = player
                    print('\n')
                    print('\t\t\tJogada válida!')
                    imprime(tabuleiro)

                    vitoria = CondVitoria(tabuleiro)

                    if vitoria == True:
                        print(player, 'ganhou, parabéns!\n')
                        serversocket.shutdown(socket.SHUT_RDWR)
                        serversocket.close()
                        break

                    if player == 'X':
                        player = 'O'

                    else:
                        player = 'X'

                else:
                    print('Vez do X')
                    while True:
                        try:
                            jogada = int(input('Jogador com o %s, digite a sua jogada:' %player))
                            break
                        except ValueError or IndexError:
                            print("Valor inválido!")
                            continue

                    if tabuleiro[jogada - 1] == '-':
                        connection.send(str(jogada).encode('utf-8'))
                        tabuleiro[jogada - 1] = player
                        print('\n')
                        print('\t\t\tJogada válida!')
                        imprime(tabuleiro)

                        vitoria = CondVitoria(tabuleiro)

                        if vitoria == True:
                            if player == 'O':
                                print("O jogador com o 'O' ganhou!")
                            else:
                                print("O jogador com o 'X' ganhou!")
                            serversocket.shutdown(socket.SHUT_RDWR)
                            serversocket.close()
                            break

                        if player == 'X':
                            player = 'O'

                        else:
                            player = 'X'

                    else:
                        print('Jogada inválida, casa ocupada, tente novamente\n')
                        continue

                if tabuleiro.count('-') == 0 and vitoria == False:
                    print('Deu empate!!!\n')
                    break
            break


def menu():

    player = 'X'
    print('\t\tJogue usando as posições: ')
    print("")
    print("\t\t      |     |     ")
    print("\t\t   7  |  8  |  9  ")
    print("\t\t _____|_____|_____")
    print("\t\t      |     |     ")
    print("\t\t   4  |  5  |  6  ")
    print("\t\t _____|_____|_____")
    print("\t\t      |     |     ")
    print("\t\t   1  |  2  |  3  ")
    print("\t\t      |     |     ")
    print("")

    while True:
        tabuleiro = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
        escolha = input('Escolha um modo de jogo:\n1 - Player vs Player (local)\n2 - Player vs Computador\n3 - Player vs Player (Remoto)\n4 - Sair\n\n')
        if escolha == '1':
            PlayerVSPlayer(player, tabuleiro)
        elif escolha == '2':
            PlayerVsAI(player,tabuleiro)
        elif escolha == '3':
            while True:

                server_client = input('Você deseja ser o (1) - Servidor ou o (2) - cliente?\nObs: O servidor jogará com o X e o Cliente com o O')
                if server_client == '2':
                    Client(player,tabuleiro)
                    break
                elif server_client == '1':
                    Server(player,tabuleiro)
                    break
                else:
                    print("Valor inválido!")
                    continue
        elif escolha == '4':
            print('Vlw')
            time.sleep(1)
            print('Flw')
            quit()
        else:
            print('Opção inválida!\n')
            continue

menu()
