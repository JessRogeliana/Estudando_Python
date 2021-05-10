
#def soma_matrizes(m1, m2):
#    if len(m1) == len(m2):
#        nova_matriz = []
#        for linha in range(len(m1)):
#            novas_linhas = []
#            for j in range(linha):
#                soma = sum(m1[j] + m2[j])
#                novas_linhas.append(soma)
#            nova_matriz.append(novas_linhas)        
#        return nova_matriz
#    else: 
#        return False 
#



def soma_matrizes(m1, m2):
    if (len(m1) == len(m2)) and (len(m1[0]) == len(m2[0])):
        nova_matriz = []
        for i in range(len(m1)):
            novas_linhas = []
            for j in range(len(m1[0])):
                soma = m1[i][j] + m2[i][j]  
                novas_linhas.append(soma)
            nova_matriz.append(novas_linhas)  
        return nova_matriz
    else: 
        return False


#m1 = [[1, 2, 5], [4, 5, 6]]
#m2 = [[2, 3], [5, 6, 7]]
#print(soma_matrizes(m1, m2))