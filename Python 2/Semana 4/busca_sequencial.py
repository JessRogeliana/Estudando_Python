def busca(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return False 

#elemento = 13
#lista = [1,2,5,4,16,3]
#print(busca(lista,elemento))
