
def solution(X, A):
    posicao = set() # Criar um set vazio
                # Guarda as posições/segundos que as folhas caem

    for i, j in enumerate(A):
        posicao.add(j)
        if len(posicao) == X:
            return i

    return -1

print(solution(5, [1, 3, 1, 4, 2, 3, 5, 4]))

