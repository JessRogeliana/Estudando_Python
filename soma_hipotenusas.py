#num** = i** + k**

def e_hipotenusa(num):
    i = 1
    while i < num:
        k = 1
        while k < num:
            if (num**2 == i**2 + k**2):    
                return True     
            k = k + 1     
        i = i + 1
    return False 


def soma_hipotenusas(n):
    i = 1
    soma = 0
    while i <= n:
        if e_hipotenusa(i) == True:
            soma = soma + i
        i = i + 1
    return soma

print(soma_hipotenusas(25))        