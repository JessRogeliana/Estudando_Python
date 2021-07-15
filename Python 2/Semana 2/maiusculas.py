
def maiusculas(frase):
    resultado = ""
    for letra in frase:
        if (letra >= "A") and (letra <= "Z"):
            resultado += letra
    return resultado 

#frase = "PrOgRaMaMoS em python!"
#print(maiusculas(frase))