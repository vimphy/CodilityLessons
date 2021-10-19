INT_RANGE = 1000000000

def solution(A):

    # Em uma lista vazia o elemento faltando deve ser 1
    if len(A) == 0:
        return 1

    # A soma dos números de 1 até o tamanho da lista mais 2 menos o tamanho da lista
    # Retorna o número que falta na sequencia
    return sum(range(1, len(A)+2)) - sum(A)

print(solution([2, 3, 1, 5]))