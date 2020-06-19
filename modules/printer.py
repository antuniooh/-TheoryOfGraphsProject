def Printar(matriz):
    result = "\n"
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            result+=("%2d" % matriz[linha][coluna] + " ")
        result+=("\n")
    result+=("\n")
    return result