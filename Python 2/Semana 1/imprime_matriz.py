def imprime_matriz(matriz):
    for linha in matriz:
        for coluna in linha:
            if coluna == linha[-1]:
                print(coluna)
            else: 
                print(coluna, end=" ")
			
#matriz = [[1,2,3],[4,5,6]]
#imprime_matriz(matriz)