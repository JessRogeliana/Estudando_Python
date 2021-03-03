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
    
def n_primos(x):
    aux2 = 2
    primos = 0
    while aux2 <= x:
        if ePrimo(aux2) == "primo":
            primos = primos + 1
        aux2 = aux2 + 1
    return primos 

#print(n_primos(121))#