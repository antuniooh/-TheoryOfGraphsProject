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

def Printar(matriz):
    for linha in range(len(matriz)): 
        for coluna in range(len(matriz[linha])): 
            print("%2d" % matriz[linha][coluna], end=" ")
        print()
    print()

def bipartido(matriz):
    m=0

def menuP():
    # menu de opções para o usuário
    print("1 - Exibir a matriz \n"
          "2 - Grafo Simples \n"
          "3 - Sequência de graus do grafo \n"
          "4 - Quantidade de Arestas \n"
          "5 - Grafo Completo? \n"
          "6 - Grafo Regular \n"
          "0 - Sair\n")

def main():
    arquivo = open("garfos.txt","r")
    matriz = []
    for linha in arquivo.readlines():
        resultado = linha.strip().split()
        matriz.append(resultado)
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
             matriz[linha][coluna] = int(matriz[linha][coluna])

    menuP()
    menu = int(input("Digite o q deseja fazer: "))
    # enquanto a variavel menu não for "0" ocorrerá a solicitação e a chamada de cada função desejada pelo usuário
    while True:
        if menu == 0:
            break
        elif menu == 1:
            Printar(matriz)
            menuP()
            menu = int(input("Digite o q deseja fazer: "))
        elif menu == 2:
            grafoSimples(matriz)
            menuP()
            menu = int(input("Digite o q deseja fazer: "))
        elif menu == 3:
            S = Sequencia(matriz)
            print("Sequência de graus do grafo: %s\n" % S)
            menuP()
            menu = int(input("Digite o q deseja fazer: "))
        elif menu == 4:
            S = Sequencia(matriz)
            Arestas(S)
            menuP()
            menu = int(input("Digite o q deseja fazer: "))
        elif menu == 5:
            S = Sequencia(matriz)
            Completo(S)
            menuP()
            menu = int(input("Digite o q deseja fazer: "))
        elif menu == 6:
            S = Sequencia(matriz)
            Regular(S)
            menuP()
            menu = int(input("Digite o q deseja fazer: "))
        else:
            print("O comando digitado não é valido\n")
            menuP()
            menu = int(input("Digite o q deseja fazer: "))
    bipartido(matriz)

main()


