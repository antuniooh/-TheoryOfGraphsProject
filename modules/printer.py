def Printar(matriz):
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            print("%2d" % matriz[linha][coluna], end=" ")
        print()
    print()