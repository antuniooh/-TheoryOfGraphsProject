from modules import printer
from modules import simpleGraph
from modules import sequence
from modules import edge
from modules import regular
from modules import complete
from modules import bipartide

def main():
    arquivo = open("grafos.txt","r")
    matriz = []
    for linha in arquivo.readlines():
        resultado = linha.strip().split()
        matriz.append(resultado)
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
             matriz[linha][coluna] = int(matriz[linha][coluna])


    printer.Printar(matriz)
    simpleGraph.grafoSimples(matriz)
    S = sequence.Sequencia(matriz)
    print("Sequência de graus do grafo em ordem não crescente: %s\n" % S)
    edge.Arestas(S)
    complete.Completo(S)
    regular.Regular(S)
    bipartide.bipartido(matriz)

if __name__ == "__main__":
    main()


