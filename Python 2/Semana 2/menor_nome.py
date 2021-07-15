def menor_nome(nomes):
    nova_lista = []
    for nome in nomes:
        nova_lista.append(nome.strip())
    menor = nova_lista[0] 
    for i in nova_lista:
        if len(i) < len(menor):
            menor = i 
    return menor.capitalize()

#print(menor_nome(['Ana ','Bárbara', 'JOSÉMAR  ', 'Billie' , '      Mariana   ']))