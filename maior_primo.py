def ePrimo(numero):
    qtd_divisiveis = 0
    aux = 1
    while (aux <= numero):
        if (numero % aux == 0):
            qtd_divisiveis = qtd_divisiveis + 1    
        aux = aux + 1
    if(qtd_divisiveis == 2):
        return "primo"
    else:
        return "não primo"
 
def maior_primo(x):
    if (ePrimo(x) == "primo"):
        return x 
    else:
        aux2 = 2
        primo = 0
        while (aux2 < x):
            if (ePrimo(aux2) == "primo"):
                primo = aux2
            aux2 = aux2 + 1
        return primo   

#print(maior_primo(10))