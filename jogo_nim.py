
def computador_escolhe_jogada(n, m):
    aux = 0
    while aux <= m: 
        if aux % (m + 1) == 0:
            return aux 
        else: 
            return m 
        aux = aux + 1



def usuario_escolhe_jogada(n, m):
    jogada_usuario = input(int("Quantas peças você vai tirar?"))
    if jogada_usuario <= m:
        return jogada_usuario
    else:
        jogada_usuario = input(int("Oops! Jogada inválida! Tente de novo"))



def partida():
    n = input(int("Quantas peças?"))
    m = input(int("Limite de peças por jogada?"))
    
    if n % (m + 1) == 0:
        print("Voce começa!")
        jogador = True
    else: 
        print("Computador começa!")   
        pc = True

    while n >= 0:
        if jogador == True:
            jogada = usuario_escolhe_jogada()
            n = n - jogada
            if n >= 1:
                print("Voce tirou", jogada , "peças.")
                print("Agora restam", n, "peças no tabuleiro.")
            else:
                return "Fim do jogo! Você ganhou!"
            jogador = False 
            pc = True
        else:
            jogada = computador_escolhe_jogada()
            n = n - jogada
            if n >= 1:
                print("O computador tirou", jogada , "peças.")
                print("Agora restam", n, "peças no tabuleiro.")
            else:
                return "Fim do jogo! O computador ganhou!"
            jogador = True
            pc = False
    


def campeonato():
    print("Voce escolheu um campeonato!")
    print("**** Rodada 1 ****")
    partida()
    print("**** Rodada 2 ****")
    partida()
    print("**** Rodada 3 ****")
    partida()
    print("**** Final do campeonato! ****")
    print("Placar: Você 0 X 3 Computador")



def jogo_nim():
    print("Bem-vindo ao jogo do NIM! Escolha:")

    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato")

    escolha = input()

    if escolha == 1:
        return partida()
    else:
        return campeonato()


jogo_nim()