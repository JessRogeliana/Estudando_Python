#duas matrizes são multiplicaveis se o numero de colunas da primeira é igual ao numero de linhas da segunda. 
#Escreva a função abaixo que recebe duas matrizes como parâmetro e devolve True se as natrizes forem multiplicadas 
#(na ordem dada) e False caso contrario. 
 
#Ex: m1 = [[123],[456]] e m2 = [[234],[567]] / False
#Ex2: m1 = [[1],[2],[3]] e m2 = [[123]] / True 

def sao_multiplicaveis(m1, m2):
    if len(m1[0]) == len(m2):
        return True
    else:
        return False 
        
m1 = [[1],[2],[3]]
m2 = [[1,2,3]]
print(sao_multiplicaveis(m1,m2))