def Regular(S):
    T=0
    for coluna in range(len(S)-1):
        if(S[coluna] == S[coluna+1]):
            T += 1
    if (T == len(S)-1):
        print("O grafo é regular, pois todos os vertices têm o mesmo grau\n")
    else:
        print("O grafo não é regular, pois todos os vertices não têm o mesmo grau\n")

