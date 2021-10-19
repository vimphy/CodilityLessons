"""
    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4
"""

def solution(N, A):
    """
    :param N: Número maximo que pode ser terá suas ocorrências contadas
    :param A: Lista com numeros inteiros
    """
    R = [0] * N   # Lista de resultados = inicialmente igual a lista com N zeros.
    m = 0         # Número máximo dos contadores no momento
    b = 0         # Número maximo de ocorrencias

    # O  contador será igual ao número maximo entre a váriavel b e o próprio contador + 1
    # se o contador inicia com zero e o número maximo de ocorrencias tambem,
    # logo o valor em questão está sendo checado pela primeira vez, sendo assim
    # o contador recebe max(b, contador) + 1 = 1. O que o indica que o número tem 1 ocorrencia

    for i in range(0, len(A)):

        # Checando se o valor que está sendo checado é menor que o número máximo permitido N
        # Caso não seja, o número máximo de ocorrencias recebe o contador com maior valor
        if A[i] <= N:
            R[A[i]-1] = max(b, R[A[i] - 1]) + 1     # R[A[i]-1] se refere ao contador do valor em questão
                                                    # na lista de Resultados R
            m = max(m, R[A[i]-1])
        else:
            b=m


    # Percorrendo a lista de resultados uma vez. Caso algum valor presente na lista for menor que
    # o número máximo de ocorrencias (b), esse valor receberar o valor de b de forma á nivelar a lista.
    for i in range(0, len(R)):
        if(R[i]<b):
            R[i]=b

    return R




