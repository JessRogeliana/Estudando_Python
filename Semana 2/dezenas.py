texto = input("Digite um número inteiro: ")
numero = int(texto)

x = numero % 100
dezenas = x // 10

print("O dígito das dezenas é", dezenas)