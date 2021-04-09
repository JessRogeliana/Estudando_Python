numero = int(input("Digite um número: "))
soma = 0

while numero > 0:
    digito = numero % 10
    soma = soma + digito
    numero = numero // 10

print(soma + numero)


# texto = input("Digite um número: ")
# tamanho = len(texto)
# numero = int(texto)
# soma = 0

# while tamanho > 0:
#     digito = numero % 10
#     soma = soma + digito
#     numero = numero // 10
#     tamanho = tamanho - 1

# print(soma)