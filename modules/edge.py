def Arestas(S):
    T=0
    for coluna in range(len(S)):
        T += S[coluna]
    return("A quantidade de arestas do grafo é : %d\n" %(T/2))
