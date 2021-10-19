"""
O numero de divisiveis por k entre dois valores A e B é igual ao número de divisiveis
por  K de 0 até A menos o número de divisiveis por K de  0 até B
"""

MAX_INT = (0, 2000000000)

def solution(A, B, K):

    """
    :param A: Inicio do intervalo
    :param B: Fim do intervalo
    :param K: Valor fixo para divisão
    """
    assert A <= B

    # Contador de divisiveis (devem ser inteiros)
    C = (int(B/K) - int(A/K))

    # Verificando se o valor inicial é divisivel por K, se for o caso é adicionado 1 ao contador de divs
    if (A%K) == 0:
        C += 1
    return C

