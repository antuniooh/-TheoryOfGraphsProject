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
