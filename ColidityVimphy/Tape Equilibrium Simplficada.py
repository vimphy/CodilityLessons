"""
    1               2
[3][1 2 4 3]    [3 1][2 4 3]

    3               4
[3 1 2][4 3]    [3 1 2 4][3]
"""

A = [3 ,1, 2, 4, 3]

def solution(A):

    # A lista deve ser ter mais que 2 elementos
    assert len(A) > 1

    fatia_1 = A[0]        # 3
    fatia_2 = sum(A[1:])  # 10
    min_diff = abs(fatia_1 - fatia_2)  # 7
    for i in range(1, len(A)-1):
        fatia_1 += A[i]  # 4, 6, 10
        fatia_2 -= A[i]  # 9, 7, 3
        diferenca = abs(fatia_1 - fatia_2)
        if diferenca < min_diff:
            min_diff = diferenca
    return min_diff

print(solution(A))
