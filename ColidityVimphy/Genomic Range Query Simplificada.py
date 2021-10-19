"""
A, C, G e T tem fatores de impacto de 1, 2, 3 e 4 respectivamente
String S = C A G C C T A
Lista P = [2, 5, 0]
Lista Q = [4, 5, 6]

a partir dos valores (x, y) entre P e Q, deve-se analisar o intervalo (x - y) afim de achar
o menor fator de impacto da fatia de string que foi cortada a partir desse intervalo
[2. 5. 0]
 |  |  |        (2, 5) - 'GCC' - Fator de impacto minimo é C = 2
[4, 5, 6]

A melhor forma de solucionar esse problema é criando uma lista para cada letra diferente
citada no enunciado, do mesmo tamanho da string original.

A = [0, 0, 0, 0, 0, 0, 0]
C = [0, 0, 0, 0, 0, 0, 0]
G = [0, 0, 0, 0, 0, 0, 0]
T = [0, 0, 0, 0, 0, 0, 0]

Após isso é percorrido string e sempre que for encontrado a letra da respectiva lista,
é adicionado 1 na mesma posição que a letra se encontra na string original

Apos isso deve-se transformar cada lista em uma lista acumulativa onde os valores são
somado um pelo outro e essa soma irá subistituir o valor em questão no percorrer da lista

A = [0 + 1 + 0 + 0 + 0 + 0 + 1]
A = [0,  1,  1,  1,  1,  1,  2]

Dessa for é possível identificar a ocorrência das letras sem ter que passar pela string
várias vezes

Assim, para cada intervalo de P,Q.
Se A[P] < A[Q] push 1 em R(resultados)
se não se C[P]<C[Q] push 2
se não se G[P]<G[Q] push 3
se não se T[P]<T[Q] push 4

Se o valor de P for igual ao valor de Q basta checar que posição da string o intervalo
se refere, Identificar a letra e push o seu fator de impacto para lista de resultados

"""
def solution(S, P, Q):

    """
    :param S: String dada na questão
    :param P: Lista de valores de X para os intervalos que serão usados
    :param Q: Lista de valores de Y para os intervalos que serão usados
    """
    # Lista de resultados
    R = []
    # listas para cada letra da string
    A = [0] * len(S)
    C = [0] * len(S)
    G = [0] * len(S)
    T = [0] * len(S)

    # Contadores para calcular os valores acumulados nas listas acima, a partir das
    # Ocorrências das letras
    a = c = g = t = 0

    # Percorrendo a string e iterando o numero +1 nas variaves acima
    # para cada ocorrência da respectiva letra
    for i in range(0, len(S)):
        if S[i] == 'A':
            a += 1
        elif S[i] == 'C':
            c += 1
        elif S[i] == 'G':
            g += 1
        elif S[i] == 'T':
            t += 1
    # No fim dos loops = a = 2 | c = 3 | g = 1 | t = 1

        A[i] = a        # A será [0 1 1 1 1 1 2]
        C[i] = c        # C será [1 1 1 2 3 3 3]
        G[i] = g        # G será [0 0 1 1 1 1 1]
        T[i] = t        # T será [0 0 0 0 0 1 1]

    # Percorrendo os intervalos de P e Q
    for i in range(0, len(P)):
        # Checando se o valor de dos intervalos é igual
        # Se for o caso é identificado qual é a string, e o seu fator de impacto
        # É adicionado na lista de resultados
        if P[i] == Q[i]:
            if S[P[i]] == 'A':
                R.append(1)
            elif S[P[i]] == 'C':
                R.append(2)
            elif S[P[i]] == 'G':
                R.append(3)
            elif S[P[i]] == 'T':
                R.append(4)

        # Checando se o valor presente nas listas na posição do valor X dos intervalos em P
        # é menor que o valot presente na listas na posição do valor Y dos intervalos
        # A = [0 1 1 1 1 1 2]
        # C = [1 1 1 2 3 3 3]                   Intervalo (P[i], Q[i]) = (1, 4)
        # G = [0 0 1 1 1 1 1]
        # T = [0 0 0 0 0 1 1]

        #  se A[1] < A[4] ou se a letra da na posição 1 dentro da string for A
        # Significa que esse é o valor de menor complexidade presente no intervalo
        # Sendo assim ele é inserido na lista de resultados
        # E o loop se repete para o proximo intervalo

        elif A[P[i]] < A[Q[i]] or S[P[i]] == 'A':
            R.append(1)
        elif C[P[i]] < C[Q[i]] or S[P[i]] == 'C':
            R.append(2)
        elif G[P[i]] < G[Q[i]] or S[P[i]] == 'G':
            R.append(3)
        elif T[P[i]] < T[Q[i]] or S[P[i]] == 'T':
            R.append(4)

    return R
    pass