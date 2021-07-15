def conta_letras(frase, contar="vogais"):
    frase = frase.replace(" ","")
    contador = 0
    if contar == "vogais":
        for palavra in frase:
            if (palavra == "a") or (palavra == "A") or (palavra == "e") or (palavra == "E") or (palavra == "i") or (palavra == "I") or (palavra == "o") or (palavra == "O") or (palavra == "u") or (palavra == "U"):
                contador += 1 
    else:
        for palavra in frase:
            if (palavra != "a") and (palavra != "A") and (palavra != "e") and (palavra != "E") and (palavra != "i") and (palavra != "I") and (palavra != "o") and (palavra != "O") and (palavra != "u") and (palavra != "U"):
                contador += 1 
    return contador 

print(conta_letras("programamos em python", "consoantes"))
