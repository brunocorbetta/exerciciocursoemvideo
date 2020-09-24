def transposta(m):
    nlinhas = (len(m))
    ncolunas = len(m[0])
    mt = []

    for i in range(0,nlinhas):
        for j in range(0,ncolunas):
            mt[j][i] = m[i][j]
        return mt

m = [[1,2,3],[4,5,6],[7,8,9]]
transposta(m)