largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))
aux_larg = largura
aux_alt = altura 

while altura > 0:
    while largura > 0:
        if altura == 1 or altura == aux_alt: 
            print("#", end="")  
        elif largura == 1 or largura == aux_larg:
            print("#", end="")
        else: 
            print(" ",end="")
        largura = largura - 1   
    print()
    altura = altura - 1
    largura = aux_larg