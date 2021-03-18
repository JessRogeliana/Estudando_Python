def remove_repetidos(lista):
    lista.sort()
    if (len(lista) > 1):
        lista.sort()
        a = []
        
        for x in lista:
            if x not in a:
                a.append(x) 
        return a
    else:
        return lista


#lista = [13, 13, 17, 24, 24, 72, -13]

#print(remove_repetidos(lista))

