INT_RANGE = (1, 1000000)

def solution(X, Y, D):
    """
    :param X: Posição inicial do SAPO
    :param Y: O ponto final minimo
    :param D: Distancia fixa a qual o sapo salta
    """
    # considerando a distancia total entre X e Y, e dividindo pelo tamanho do pulo
    # conseguiremos o número de pulos necessários para responder a questão,
    # sem precisar percorrer a lista várias vezes
    # Porém se deve ser checado se o valor calculado na formula(v)
    # multiplcado pelo valor de um único pulo, excede o valor da distancia final Y
    # Caso seja pode ser que a funçao retorne número de pulos menor que o mínimo
    # requerido para percorrer a distancia
    # logo deve ser adicionado +1 ao número de pulos (v) calculados

    # Floor division (//) garante que o calculo dos pulos seja um inteiro não float
    # (Y - X) referese a distancia entre X e Y sendo X > Y
    # Dividindo esse valor pela distancia de cada pulo (D) resultará
    # o numero de pulos necessarios.
    v = (Y - X) // D

    # é checado se o número de pulos (v) é maior ou igual
    # a soma da posição inicial do sapo + o número de pulos calculados
    # multiplicado pela distancia do pulo que foi dada
    # assim garantindo que se por exemplo x = 1 e Y 6 e a distancia do pulo (D_ seja 4
    # não haja um valor menor de pulos como resultado
    if X + v * D >= Y:
        return v
    else:
        return v+1
pass

print(solution(10, 85, 30))