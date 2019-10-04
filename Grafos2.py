
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
    #a quantidade de arestas é a soma dos graus dos vertices sobre dois
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

def bipartidoCompleto(x, y, matriz):
    boolBpCompleto = True

    for i in range(len(x)):
        cont = 0
        for j in range(len(y)):
            k = x[i]
            z = y[j]
            if matriz[k][z] > 0:
                cont+=1
        if cont < len(y):
            boolBpCompleto = False
            break

    if boolBpCompleto:
        print("\nO grafo é bipartido completo, pois cada vértice com bipartição em x se conecta a todos os vértices com bipartição em y.")
    else:
        print("\nO grafo não é bipartido completo, pois nem todo vértice com bipartição em x se conecta a todos os vértices com bipartição em y.")

def bipartido(matriz):
    boolBipartido = True
    x =[]
    y =[]

    def findAdjacentes(y):
        if len(y) > 1:
            for i in range(len(y)):
                for j in range(len(y)):
                    z = y[i]
                    k = y[j]
                    if matriz[z][k] != 0:
                        return True
        return False

    for i in range(len(matriz)):
        if i not in y:
            x.append(i)
            for j in range(len(matriz)):
                if j > i:
                    if matriz[i][j] > 0:
                        if j not in y:
                            y.append(j)
        if findAdjacentes(y):
            boolBipartido = False

    if boolBipartido:
        print("\nO grafo é bipartido, e possui bipartições em x = {", end="")
        for i in range(len(x)):
            if i < len(x)-1:
                print("v{}".format(x[i]+1), end=", ")
            else:
                print("v{}".format(x[i]+1), end="} e y = {")

        for j in range(len(y)):
            if j < len(y)-1:
                print("v{}".format(y[j] + 1), end=", ")
            else:
                print("v{}".format(y[j] + 1), end = "}")

        bipartidoCompleto(x, y, matriz)


    else:
        print("\nO grafo não é bipartido, pois possui vértices que se conectam a n vértices adjacentes.")

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
