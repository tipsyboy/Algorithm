import sys
import time

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


# 정사각행렬 곱
def mul_square_matrix(matrix_a, matrix_b):
    size = len(matrix_a)
    matrix = [[0] * size for _ in range(size)]

    for i in range(size):
        for j in range(size):
            for k in range(size):
                matrix[i][j] += matrix_a[i][k] * matrix_b[k][j]

    return matrix


def fibonacci(n):
    def power_matrix(matrix, exp):
        # 1) base case
        if exp == 1:
            for i in range(len(matrix)):
                for j in range(len(matrix)):
                    matrix[i][j] %= 1_000_000_007

            return matrix

        # 2) base case가 아닌 경우 //2 로 재호출
        temp = power_matrix(matrix, exp // 2)
        # 3) 받아온 matrix 제곱
        temp = mul_square_matrix(temp, temp)

        # 4) exp 홀수 처리
        if exp % 2 != 0:
            temp = mul_square_matrix(temp, base)

        for i in range(len(temp)):
            for j in range(len(temp)):
                temp[i][j] %= 1_000_000_007

        return temp

    ###
    if n < 2:
        return n

    base = [[1, 1], [1, 0]]

    return power_matrix(base, n)[0][1]


n = int(input())
# start = time.time()
print(fibonacci(n))
# print(time.time() - start)


"""
47. 11444 피보나치 수 6 (Gold 3)
    - 굉장히 큰 수 번째 피보나치 수를 구하는 문제

    - 피보나치 수를 행렬 곱을 통해서 구하는 방법을 알고 큰 수 거듭제곱을 사용한다. 

    - 피보나치 수를 행렬을 통해서 나타내는 방법을 이해하면, 10830 행렬 제곱 문제와 같은 문제이다. 
"""