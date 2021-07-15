def ordena(lista):
    fim = len(lista)
    for i in range(fim-1):
        minimo = i
        for j in range(i+1, fim):
            if lista[j] < lista[minimo]:
                minimo = j
        lista[i], lista[minimo] = lista[minimo], lista[i]
    return lista 

#lista = [9,1,27,49,59,1,1000,200,1967,2000,600,139] 
#print(ordena(lista))
