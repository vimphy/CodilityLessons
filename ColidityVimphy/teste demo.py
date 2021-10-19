def solution(A):
    for i in range(100000):
        if i > 0 and i not in A:
            return i


print(solution([1, 3, 6, 4, 1, 2]))