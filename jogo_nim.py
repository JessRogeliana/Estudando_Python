
def computador_escolhe_jogada(n, m):
    pecas = 1
    while pecas <= m: 
        sobra = n - pecas
        if sobra % (m + 1) == 0:
            return pecas
        pecas = pecas + 1                               
    if n <= m:
        return n 
    else: 
        return m 



def usuario_escolhe_jogada(n, m):
    jogada_usuario = int(input("Quantas peças você vai tirar?"))
    
    while ((jogada_usuario > m) or (jogada_usuario <= 0)):
        print("Oops! Jogada inválida! Tente de novo")
        jogada_usuario = int(input("Quantas peças você vai tirar?"))
    return jogada_usuario



def partida():
    n = int(input("Quantas peças?"))
    m = int(input("Limite de peças por jogada?"))
    
    jogador = False
    pc = False 

    if n % (m + 1) == 0:
        print("Voce começa!")
        jogador = True
    else: 
        print("Computador começa!")   
        pc = True

    while n > 0:
        if jogador == True:
            jogada = usuario_escolhe_jogada(n,m)
            n = n - jogada
            if n >= 1:
                print("Voce tirou", jogada , "peças.")
                print("Agora restam", n, "peças no tabuleiro.")
            else:
                print("Fim do jogo! Você ganhou!")
            jogador = False 
            pc = True
        else:
            jogada = computador_escolhe_jogada(n,m)
            n = n - jogada
            if n >= 1:
                print("O computador tirou", jogada , "peças.")
                print("Agora restam", n, "peças no tabuleiro.")
            else:
                print("Fim do jogo! O computador ganhou!")
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

    escolha = int(input())
    
    if escolha == 1:
        return partida()
    else:
        return campeonato()
    

jogo_nim()