numero = input(int("Digite um número"))
lista = []


while numero > 0:
    lista.append(numero)
    numero = input(int("Digite um número"))       
    lista.sort(reverse = true)
    
    if numero == 0:
        print(lista)


