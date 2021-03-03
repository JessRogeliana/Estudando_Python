
def computador_escolhe_jogada(n, m):
    aux = 0
    while aux <= m: 
        if (m + 1) % aux == 0:
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
    i = 0
    while i <= m: 
        if (m + 1) % i == 0:
            return("Computador começa!") #True ?
        else: 
            return("Voce começa!") #False ?
        aux = aux + 1
    #if return True print("Computador começa!") (?)
    if 
    

def campeonato():


print("Bem-vindo ao jogo do NIM! Escolha:")

print("1 - para jogar uma partida isolada")
print("2 - para jogar um campeonato 2")
