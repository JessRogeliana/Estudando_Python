#Pegar o numero e ir diminuido e comparando se são iguais#
#Se sim printar, se não continuar#

texto = input("Digite um número: ")
quantidade_casas = len(texto)
numero = int(texto)
adjacente = False  

while (quantidade_casas > 1):
    if (numero  % 10 ) == ((numero // 10) % 10):
        adjacente = True 
    else: 
        numero = numero // 10
    quantidade_casas = quantidade_casas - 1

if (adjacente):
    print("sim") 
else: 
    print("não")   
