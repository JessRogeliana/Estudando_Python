def maior_elemento(lista):
    lista.sort()
    return lista[-1]

lista = [13, 13, 17, 24, 24, 72, -13]

print(maior_elemento(lista))
