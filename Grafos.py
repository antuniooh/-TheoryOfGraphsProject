matriz=[] 
num = 0 
m = []

def grafoSimples(matriz):
    for linha in range(len(matriz)): 
        for coluna in range(len(matriz[linha])):
            if(linha == coluna and matriz[linha][coluna] == 1):
                print("Há laço no vertice %s" %(linha+1))
            else:
                pass

    for linha in range(len(matriz)): 
        for coluna in range(len(matriz[linha])):
            if(matriz[linha][coluna] > 1):
                print("Há aresta multiplas nos vertices %s %s" %((linha+1), (coluna+1)))
            else:
                pass

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
    return int(T/2)

def Completo(S):
    T=0
    for coluna in range(len(S)):
        if(S[coluna] == (len(S) - 1)):
            T += 1
            
    if (T == len(S)):
        print("A matriz é completa, pois todos os vertices incidem sobre todos os outros")
    else:
        print("A matriz não é completa, pois todos os vertices não incidem sobre todos os outros")

def Regular(S):
    T=0
    for coluna in range(len(S)-1):
        if(S[coluna] == S[coluna+1]):
            T += 1
    if (T == len(S)-1):
        print("A matriz é regular, pois todos os vertices têm o mesmo grau")
    else:
        print("A matriz não é regular, pois todos os vertices não têm o mesmo grau")

def Printar(matriz):
    for linha in range(len(matriz)): 
        for coluna in range(len(matriz[linha])): 
            print("%2d" % matriz[linha][coluna], end=" ")
        print()
    

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
print("Sequencia de graus do grafo: %s" %S)
A = Arestas(S)
print("O número de arestas do grafo: %s" %A)
Completo(S)
Regular(S)


