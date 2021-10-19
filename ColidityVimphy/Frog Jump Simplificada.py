INT_RANGE = (1, 1000000)

def solution(X, Y, D):
    """
    :param X: Posição inicial do SAPO
    :param Y: O ponto final minimo
    :param D: Distancia fixa a qual o sapo salta
    """

    # Assuma que X é menor ou igual a Y
    assert X <= Y

    # Com a utilização da função divmod obtemos o quociente da divisão entre a distancia que precisa ser percorrida
    # (ou seja, a distancia minima do final menos o ponto inicial)
    # E o tamnho fixo dos pulos do sapo. Sabem assim quantos pulos devcm ser dados no mínimo (quociente)
    coef, resto = divmod(Y - X, D)
    return coef if resto == 0 else coef + 1

