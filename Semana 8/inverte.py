numero = int(input("Digite um número: "))

lista = []


while numero != 0:
    lista.append(numero)
    numero = int(input("Digite um número: "))       
    if numero == 0:
        lista.reverse()
        for x in lista:
            print(x)

