#def remove_repetidos(lista):
#    lista.sort()
#    a
#    for x in lista:
#        if 

def remove_repetidos (lista):
    
    if (len(lista) > 1):
        lista.sort()
        print(lista)
        elemento_anterior = lista[-1]

        for i, item in enumerate(lista):
            print("i", i)
            print("item", item)
            if (item == elemento_anterior):
                del lista[i]
                print("lista", lista)
            else:
                elemento_anterior = item
    else:
        return lista
        


lista = [12, 14, 12, 12, 13, 13, 11]

print(remove_repetidos(lista))

