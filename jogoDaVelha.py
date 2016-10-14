tabuleiro = ['', '1', '2', '3',
             '4', '5', '6', '7',
             '8', '9', '2', ' ', ]

jogadas_possiveis = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

jogadas = 1
jogador_da_vez = 0

vitorias_um = 0
vitorias_dois = 0
empates = 0

jogadores = []


def imprime():
    print("")
    print("\t\t      |     |     ")
    print("\t\t   %s  |  %s  |  %s " % (tabuleiro[7], tabuleiro[8], tabuleiro[9]))
    print("\t\t _____|_____|_____")
    print("\t\t      |     |     ")
    print("\t\t   %s  |  %s  |  %s " % (tabuleiro[4], tabuleiro[5], tabuleiro[6]))
    print("\t\t _____|_____|_____")
    print("\t\t      |     |     ")
    print("\t\t   %s  |  %s  |  %s " % (tabuleiro[1], tabuleiro[2], tabuleiro[3]))
    print("\t\t      |     |     ")
    print("")


def limpar_tabuleiro():
    for l in range(11):
        tabuleiro[l] = " "


def jogada(pos, jogador_da_vez):
    while True:
        if tabuleiro[pos] == ' ':
            print(jogador_da_vez)
            if jogador_da_vez == 0:
                tabuleiro[pos] = 'X'
                return 1
            elif jogador_da_vez == 1:
                tabuleiro[pos] = "O"
                return 0
            break
        else:
            print("\n" * 80)
            imprime()
            pos = int(input("ops posicao ocupada, tente novamente:  \n"))
    print("\n" * 60)


def testa_pocicoes(lista=[]):
    """Como a estrutura para verificar é a mesma, esta funcao apenas reecebe a lista que contem as cordenadas possiveis para vitorias
    sendo elas as horizontais, verticais e diagonal... """

    for cordenadas in lista:
        # variaveis que vao receber as coordenadas das listas que estao na funcao vencedor...
        x0 = cordenadas[0]
        x1 = cordenadas[1]
        x2 = cordenadas[2]

        if tabuleiro[x0] == tabuleiro[x1] == tabuleiro[x2]:
            # caso entre aqui é porque ele encontrou uma repetição, agora basta saber qual jogador ganhou, testado uma delas ja que todas sao iguais... X ou 0

            if tabuleiro[x0] == "X":
                return 1
            elif tabuleiro[x0] == "O":
                return 2
    return None


def vencedor():
    """
    vemos as cordenadas, com isso da pra entender as listas abaixo que contem as possiveis sequencias de vitoria, de ambos os jogadores
    	      |     |
		   7  |  8  |  9
		 _____|_____|_____
		      |     |
		   4  |  5  |  6
		 _____|_____|_____
		      |     |
		   1  |  2  |  3
		      |     |
    """

    lista_cordenadas_horizontal = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    lista_cordenadas_vertical = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    lista_cordendas_diagonal = [[7, 5, 3], [9, 5, 1]]

    resultado_horizontal = testa_pocicoes(lista_cordenadas_horizontal)
    if not resultado_horizontal == None:
        return resultado_horizontal

    resultado_vertical = testa_pocicoes(lista_cordenadas_vertical)
    if not resultado_vertical == None:
        return resultado_vertical

    resultado_diagonal = testa_pocicoes(lista_cordendas_diagonal)
    if not resultado_diagonal == None:
        return resultado_diagonal


jogador1 = input("Nome do primeiro jogador: ")
jogador2 = input("Nome do segundo jogador: ")
jogadores.append(jogador1)
jogadores.append(jogador2)

while True:

    imprime()
    limpar_tabuleiro()
    imprime()

    while True:

        if jogadas <= 9:

            while True:
                pos = input(" Uma jogada %s: " % jogadores[jogador_da_vez])

                if pos in jogadas_possiveis:
                    pos = int(pos)
                    break
                else:
                    print("\n" * 80)
                    imprime()
                    print("***POSICAO INVALIDA*** Jogue novamente")

            jogador_da_vez = jogada(pos, jogador_da_vez)
            imprime()
            venceu = vencedor()
            if venceu == 1:
                print("parabens %s" % jogadores[0])
                vitorias_um += 1
                break
            elif venceu == 2:
                print("parabens %s" % jogadores[1])
                vitorias_dois += 1
                break
            elif jogadas > 9:

                break
            else:
                jogadas += 1
        else:
            print("Partida empatada,nenhum vencendor")
            empates += 1
            break

    escolha = input("Deseja jogar novamente com os mesmos jogadores S/N, se deseja sair aperte outra tecla")
    if escolha.upper() == 'N':
        jogador1 = input("Nome do primeiro jogador:  ")
        jogador2 = input("Nome do segundo jogador:  ")
        jogadores = jogador1, jogador2
        jogadas = 1
    elif escolha.upper() == 'S':
        print("")

        jogadas = 1
    else:
        break

print("\n" * 60)

print("Fim de Jogo")
print()
print("empates ", empates)
print("Vidorias de %s = %d" % (jogadores[0], vitorias_um))
print("Vidorias de %s = %d" % (jogadores[1], vitorias_dois))