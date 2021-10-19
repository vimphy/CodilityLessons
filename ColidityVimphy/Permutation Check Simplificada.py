# Permutation é uma sequencia de números que contem cada elemento apenas uma vez


def solution(A):

    # Checar se a lista não é nula
    if len(A)==0:
        return 0

    # Organizar a lista de forma crescente
    A.sort()

    # Percorrer a lista
    for i in range(0, len(A)):
        # checar se os indices da lista quando somados a 1 são iguais ao valor do item
        # Isso mostra que a os itens seguem uma sequencia e que ocorrem uma unica vez na lista
        if A[i] != (i+1):
            return 0

    return 1
    pass




print(solution([3,2,1]))