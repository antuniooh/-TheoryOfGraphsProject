from modules import printer
from modules import simpleGraph
from modules import sequence
from modules import edge
from modules import regular
from modules import complete
from modules import bipartide

def resultValues(textFile):
    arquivo = open("./graphs/" + textFile,"r")
    matriz = []
    for linha in arquivo.readlines():
        resultado = linha.strip().split()
        matriz.append(resultado)
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
             matriz[linha][coluna] = int(matriz[linha][coluna])

    result = ""
    result += printer.Printar(matriz)
    result += simpleGraph.grafoSimples(matriz)
    S = sequence.Sequencia(matriz)
    result += ("Sequência de graus do grafo em ordem não crescente: %s\n" % S)
    result += edge.Arestas(S)
    result += complete.Completo(S)
    result += regular.Regular(S)
    result += bipartide.bipartido(matriz)
    return(result)



