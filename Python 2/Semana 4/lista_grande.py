import random

def lista_grande(n):
    lista = []
    while n > 0:
        lista.append(random.randint(0,100))
        n-=1 
    return lista 

#print(lista_grande(3))