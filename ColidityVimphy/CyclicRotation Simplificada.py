def solution(A, K):
    """
    :param A: Lista de inteiros
    :param K: Número de rotações que devem ser executadas
    """

    """
    Soluçào bruta:
    for each K
        for each i
            A[i+1] = A[1]
    and A[0] = last element fo A
    
    nessa solução estamos repitiondo a mudança de posição da lista K vezes
    O que deixa de a solução muito complicada
    """

    """
    Dada o valor de K = 3
    e A inicial = [ 3, 8, 9, 7, 6]
    primeira rotação = [6, 3, 8, 9, 7]
    segunda rotaçào = [7, 6, 3, 8, 9]
    e A na rotação final = [9, 7, 6, 3, 8]
    
    Durante as rotações, o indice de cada elemento está mudando a a partir 
    da soma do seu ultimo indice + o valor de K módulo(%) o tamanho da lista
    
    O cálculo do módulo garante que sempre que um indice é incrementado, se o mesmo 
    exceder o tamanho da lista, o elemento correspondente é levado de volta ao inicio
    da lista
    
    Com a lista exemplo [3, 8, 9, 7, 6]
    o indice de 9 é [2] somado a K (3) modulo tamanho da lista(5)
    O indice o qual 9 era será alocado será 0.
    
    Lista final =  [9, 7, 6, 3, 8]
    
    
    Better Solution
    
    para cada elemento de A
        mova seu indice para a posição final do ciclo
    """
    # Checar se A estã vazio

    if not len(A):
        return A

    # Tamanho da lista
    N = len(A)
    # Cópia da lista A para usar como referencia após a modificação de A pelas rotações
    B = [None] * N

    for i in range(0, N):
        B[(i + K) % N] = A[i]
        print(f'O valor de {i} irá para a posição {(i + K) % N}.')
        print(B)
    return B

solution([3, 8, 9, 7, 6], 3)



#     netK = (len(A) + K) % len(A)
#
#     if netK > 0:
#         head = A[len(A) - netK:]
#         tail = A[:-netK]
#         return head + tail
#     else:
#         return A
#
#
# print(solution([3, 8, 9, 7, 6], 3))