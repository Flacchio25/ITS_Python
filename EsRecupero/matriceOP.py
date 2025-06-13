def diag(M:list[list[int]])-> int:
    somma:int = 0
    for i in range(len(m)):
        somma += M[i][i]

        somma2+= M[i][len(M)-1-i]

        return somma
    