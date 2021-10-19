MAX_INT = (1000000)

def solution(A):
    # Variavél que representa a soma dos carros indo para o leste
    sL = 0
    # O valor total de carros atravessando de leste para oeste(pares)
    pares = 0

    for i in range(0, len(A)):

        # Se o Valor for igual a 0, significa um carro indo para leste, logo a variável é incrementada
        if A[i] == 0:
            sL += 1
        # Se o valor for 1 significa que um par foi encontrado
        # A variavel sL é responsável por indicar de quantos pares aquele elemento irá fazer parte
        # Se sL = 2 então o número 1 em questão formará 2 pares
        elif A[i] == 1:
            pares += sL

    if pares > 1000000000:
        return -1
    else:
        return pares
    pass


print(solution([0, 1, 0, 1, 1, 1]))