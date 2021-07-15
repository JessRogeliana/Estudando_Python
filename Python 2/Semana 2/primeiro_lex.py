def primeiro_lex(lista):
    resultado = lista[0]
    for item in lista:
        if item < resultado:
            resultado = item
    return resultado

#lista = ['oĺá', 'A', 'a', 'casa']
#print(primeiro_lex(lista))
