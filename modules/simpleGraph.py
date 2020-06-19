def grafoSimples(matriz):
    l = 0
    am = 0
    for linha in range(len(matriz)): 
        for coluna in range(len(matriz[linha])):
            if(linha == coluna and matriz[linha][coluna] == 2):
                print("Há laço no vertice %s\n" %(linha+1))
                l = 1
            if (linha != coluna and matriz[linha][coluna] > 1):
                print("Há aresta multiplas nos vertices %s %s\n" % ((linha + 1), (coluna + 1)))
                am = 1

    if am == 0 and l ==0:
        print("É um grafos simples, pois não possui arestas multiplas e laços\n")
    else:
        print("Não é um grafos simples, pois possui arestas multiplas e laços\n")
