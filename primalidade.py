#primo é divisivel apenas por 1 e por ele mesmo#

numero = int(input("Digite um número inteiro: "))
qtd_divisiveis = 0
aux = 1

while (aux <= numero):
    if (numero % aux == 0):
        qtd_divisiveis = qtd_divisiveis + 1    
    aux = aux + 1

if(qtd_divisiveis == 2):
    print("primo")
else:
    print("não primo")
