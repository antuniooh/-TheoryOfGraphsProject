def Printar(matriz):
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            print("%2d" % matriz[linha][coluna], end=" ")
        print()
    print()

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

def Arestas(S):
    T=0
    for coluna in range(len(S)):
        T += S[coluna]
    print("A quantidade de arestas do grafo é : %d\n" %(T/2))

def Completo(S):
    T=0
    T = S.count(len(S)-1)

    if (T == len(S)):
        print("O grafo é completo, pois todos os vertices incidem sobre todos os outros\n")
    else:
        print("O grafo não é completo, pois todos os vertices não incidem sobre todos os outros\n")

def Regular(S):
    T=0
    for coluna in range(len(S)-1):
        if(S[coluna] == S[coluna+1]):
            T += 1
    if (T == len(S)-1):
        print("O grafo é regular, pois todos os vertices têm o mesmo grau\n")
    else:
        print("O grafo não é regular, pois todos os vertices não têm o mesmo grau\n")


def bipartido(matriz):
    Bipartido = True
    u =[]
    v =[]

    def adjacentes(y):
        if len(v) > 1:
            for i in range(len(v)):
                for j in range(len(v)):
                    z = v[i]
                    k = v[j]
                    if matriz[z][k] != 0:
                        return True
        return False

    for i in range(len(matriz)):
        if i not in v:
            u.append(i)
            for j in range(len(matriz)):
                if j > i:
                    if matriz[i][j] > 0:
                        if j not in v:
                            v.append(j)
        if adjacentes(v):
            Bipartido = False

    if Bipartido:
        print("O grafo é bipartido, e possui bipartições em u = {", end="")
        for i in range(len(u)):
            if i < len(u)-1:
                print("V{}".format(u[i]+1), end=", ")
            else:
                print("V{}".format(u[i]+1), end="} e V = {")

        for j in range(len(v)):
            if j < len(v)-1:
                print("V{}".format(v[j] + 1), end=", ")
            else:
                print("V{}".format(v[j] + 1), end = "}")
        print("\n")

        def bipartidoCompleto(u, v, matriz):
            BipCompleto = True

            for i in range(len(u)):
                cont = 0
                for j in range(len(v)):
                    k = u[i]
                    z = v[j]
                    if matriz[k][z] > 0:
                        cont+=1
                if cont < len(v):
                    BipCompleto = False
                    break

            if BipCompleto:
                print("O grafo é bipartido completo, pois cada vértice com bipartição em u se conecta a todos os vértices com bipartição em v\n")
            else:
                print("O grafo não é bipartido completo, pois não são todos os vértices com bipartição em u que se conectam a todos os vértices com bipartição em v\n")

        bipartidoCompleto(u, v, matriz)


    else:
        print("O grafo não é bipartido, pois possui vértices que se conectam a vértices adjacentes\n")

def main():
    arquivo = open("garfos.txt","r")
    matriz = []
    for linha in arquivo.readlines():
        resultado = linha.strip().split()
        matriz.append(resultado)
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
             matriz[linha][coluna] = int(matriz[linha][coluna])


    Printar(matriz)
    grafoSimples(matriz)
    S = Sequencia(matriz)
    print("Sequência de graus do grafo em ordem não crescente: %s\n" % S)
    Arestas(S)
    Completo(S)
    Regular(S)
    bipartido(matriz)
main()


