import time

tabuleiro = ['-', '-', '-', '-', '-', '-', '-', '-', '-']


def imprime():
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


'''def test():
    assert CondVitoria(list("XXX---OOO")) == True
    assert CondVitoria(list('X---OO--X')) == False
    assert CondVitoria(list('X--X--X--')) == True
    assert CondVitoria(list('X-O-OO--X')) == False
    assert CondVitoria(list('X-OOX--OX')) == True
    assert CondVitoria(list('X-OOO-O-X')) == True
    assert proximaJogada(list('X----O-XO'), 'X') == (1, 2)
    assert proximaJogada(list('OXX---XOO'), 'X') == (1, 4)
    assert proximaJogada(list('XX---OO-O'), 'X') == (1, 2)
    assert proximaJogada(list('---------'), 'X') == (0, 4)
    assert proximaJogada(list('XXOOO-XO-'), 'X') == (0, 5)
    assert proximaJogada(list('OO-XXO-XO'), 'X') == (0, 2)
    assert proximaJogada(list('XX-OO-XO-'), 'O') == (-1, 5)
    assert proximaJogada(list('XX--O-XOO'), 'O') == (1, 2)
    return "Casos de teste passados"
    '''


global player
player = 'X'


def PlayerVsAI(player,tabuleiro):
    imprime()
    while True:
        proximo = proximaJogada(tabuleiro, player)
        if proximo[1] != -1:
            if player == 'O':
                proximo = proximaJogada(tabuleiro, player)
                print('MinMax jogando')
                jogada = proximo[1] + 1

            else:

                jogada = int(input('Digite a jogada:'))

            if tabuleiro[jogada - 1] == '-':
                tabuleiro[jogada - 1] = player
                imprime()

                vitoria = CondVitoria(tabuleiro)

                if vitoria == True:
                    print(player, 'ganhou')
                    for j in range(len(tabuleiro)):
                        tabuleiro[j] = '-'
                    quit()

                if player == 'X':
                    player = 'O'

                else:
                    player = 'X'


            else:
                continue
        else:
            print('Deu empate!!!')
            for j in range(len(tabuleiro)):
                        tabuleiro[j] = '-'
            break

def PlayerVSPlayer(player,tabuleiro):
    imprime()
    while True:
            jogada = int(input('Player com '+player+' digite a jogada: '))

            if tabuleiro[jogada - 1] == '-':
                tabuleiro[jogada - 1] = player
                imprime()

            else:
                print('Jogada inválida')
                continue

            vitoria = CondVitoria(tabuleiro)

            if vitoria == True:
                print(player, 'ganhou')
                for j in range(len(tabuleiro)):
                        tabuleiro[j] = '-'
                quit()

            if player == 'X':
                player = 'O'

            else:
                player = 'X'

            if tabuleiro.count('-') == 0 and vitoria == False:
                print('Deu empate!!!')
                for j in range(len(tabuleiro)):
                        tabuleiro[j] = '-'
                break

def menu():

    escolha = input('Qual modo de jogo vocẽ quer?\n1 - Player vs Player (local)\n2 - Player vs Computador\n3 - Player vs Player (Remoto)\n4 - Sair\n\n')
    if escolha == '1':
        PlayerVSPlayer(player,tabuleiro)
    elif escolha == '2':
        PlayerVsAI(player,tabuleiro)
    elif escolha == '3':
        print('Em obras')
    elif escolha == '4':
        print('Vlw')
        time.sleep(1)
        print('Flw')
        quit()
    else:
        print('Escolha errada')

while True:
    menu()
