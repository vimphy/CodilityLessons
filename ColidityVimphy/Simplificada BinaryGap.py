"""
Sequencia maxima de zeros consecutivos

Primeiro devemos ler a sequencia de numeros
Incrementamos uma variavel auxiliar para cada zero encontrado
Resetar o contador, toda a vez que 1 for encontrado
A cada loop, devemos comparar o valor do contador de zeros com o valor maximo atual
"""

def solution(N):
    # utilizando a funcão bin para transformar o numero em binario
    # N recebe o a conversão a partir do indice 2 do número já que os 2 primeiros números
    # quando convertidos para binário com a função bin são 0b
    N = bin(N)[2:]
    print(N)
    # contador de ocorrencias de 0
    b = 0
    # variavel que guarda o valor máximo de 0 consecutivos
    maxb = 0
    for k in N:
        if int(k) == 0:
            b += 1
            print([0]*b)
        elif int(k) == 1:
            maxb = max(b, maxb)
            b = 0
    print(f'Número maximo de zeros entre 1 = {maxb}')
    return maxb


solution(69)