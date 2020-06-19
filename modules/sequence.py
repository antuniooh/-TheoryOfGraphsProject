def Sequencia(matriz):
    sequencia= []
    grau=0
    for linha in range(len(matriz)): 
        for coluna in range(len(matriz[linha])):
            grau+=matriz[linha][coluna]
        sequencia.append(grau)
        grau=0    
    sequencia.sort(reverse=True)
    return sequencia
