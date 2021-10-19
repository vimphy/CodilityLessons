N_RANGE = (1, 100000)
ELEMENT_RANGE = (-2147483648, 2147483647)


def solution(A):
    """
    :param A: lista não vazia composta por numeros inteiros
    :return: Um inteiro - O menor número inteiro positivo que falta
    """

    # Assumindo que o número que falta é 1
    faltando = 1

    # Percorrendo a lista organizada para facilitar a identificação do elemento
    for elemento in sorted(A):

        # Se o elemento presente na lista for igual a variavel faltando siginifica que ordem está sendo seguida
        if elemento == faltando:
            faltando += 1
        # Se o elemento for maior que a variavel faltando significa que um número da ordem foi pulado
        # Sendo assim o valor atual da variável faltando é o valor que minimo positivo que falta
        if elemento > faltando:
            break
    return faltando
