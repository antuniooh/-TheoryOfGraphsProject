def Completo(S):
    T=0
    T = S.count(len(S)-1)

    if (T == len(S)):
        return("O grafo é completo, pois todos os vertices incidem sobre todos os outros\n")
    else:
        return("O grafo não é completo, pois todos os vertices não incidem sobre todos os outros\n")
