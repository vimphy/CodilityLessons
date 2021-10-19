"""
Dado uma lista A com N valores inteiros, achar a posição onde está localizada
a média mínima encontrada na soma entre combinações de itens da lista

A = [4, 2, 2, 5, 1, 5, 8]

dado o intervalo de indices (1, 4) - [2, 2, 5, 1]
A média minima encontrada a partir da soma de dos itens presentes no intervalo é 2
onde a combinação soma dos valores(2+2) dividida pelo tamanho da fatia ou intervalo (4)
é igual a 2

Somente intervalos de 2 ou 3 elementos precisam ser testatos pois somente essas combinações
gerarão uma média mínima

Intervalos de 4 ou mais elementos sempre terão combinações menores que quando calculadas
Gerarão uma média menor que a média dos números calculados no intervalo total

Assim para cada elemento de A que será percorrido
será calculada a média (av) entre esse elemento e 2 elementos a mais (A[i]+A[i+1]+A[i+2])
e outra média calculando somente de 1 elemento a frente (A[i]+A[i+1])
O valor mínimo é salvado e a iteração continua

O loop será feito até o ante penultimo item da lista (A[i-2]) para que a não se exceda
o tamanho da lista durante os calculos

Ao final do loop os 2 ultimos itens da lista serão testados, tendo em visa que oos mesmos
foram ignorado no loop anterior, ao contrário, o tamanho da lista seria excedida


"""


MAX_INT = (100000)
MAX_RANGE = (-10000, 10000)

def solution(A):

    # Resultado, média mínima encontrada
    mn = MAX_INT
    # Indice inicial da média mínima, valor que o problema pede
    mi = 0

    # percorrendo a lista utilizando o principio de intervalos e 2 ou 3 valores
    for i in range(0, len(A)-2):
        v1 = (A[i] + A[i+1] + A[i+2]) / 3
        v2 = (A[i] + A[i+1]) / 2
        if mn > v1 or mn > v2:
            mn = min(v1, v2)
            mi = i
    # Calculando a média dos dois ultimos itens da lista que foram préviamente ignorados
    if mn > (A[-1] + A[-2]) / 2:
        return len(A)-2

    return mi
    pass
