import random

MAX_LENGTH = 1000000

"""
Solução bruta seria interar cada valo até achar seu par igual, quando tal, seria tirado da lista o
o par. Se sobrasse algum elemento na lista no fim da operação, o mesmo seria o sem par
[9, 3, 5, 6, 5, 3, 9]
O par de 9 por exemplo é encontrado somente no fim do loop

Um solução mais eficiente comecaria ordenando a lista em ordem crescente
dessa forma, o par de cada elemento ficaria um indice a sua frente.
Caso seja identificado um elemento que não tenha seu par igual um indice a frente esse seria
o número procurado.

[3, 3, 5, 5, 6, 9, 9]
Dessa forma fica mais facil identificar o par de cada elemento. Se o elemento vizinho
for o par do elemento em questão, pulasse o indice do atual + 2 pulando seu par.

"""

def solution(A):

    # Verificando se a lista tem tamanho 1
    if len(A) == 1:
        return A[0]
    # Ordenar a lista
    A.sort()
    # Adicionar -1 ao fim da lista de forma que o último valor será comparado a ele
    # Sendo certamente diferente, isso garante que se caso o último número da lista
    # for o número sem par, o mesmo possa ser identificado sem que o iterador
    # ultrapasse o tamanho da lista.
    A.append(-1)

    # Percorrer a lista de pulando de 2 em 2 indices com o objetivo de pular o par
    # Caso encontrado
    for i in range(0, len(A), 2):
        # Se o valor de A[i] for diferente de A[i + 1], significa que A[i] é o valor odd
        if A[i] != A[i+1]:
            return A[i]

    pass

"""
Terceira solução

def solution(A):
    if len(A) == 1:
        return A[0]
    
    A.sort()
    
    nesse caso faremos o loop até o penultimo indice da lista
    assim caso o ao fim do loop não seja encontrado o valor diferente 
    após o fim do loop, o valor de -1, ou seja, o último valor serã retornado
    for i in range(0, len(A)-1, 2:
        if A[i] != A[i+1]:
            return A[i]
    return A[-1]
    pass
"""
