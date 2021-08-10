import sys

input = sys.stdin.readline


def multiple_matrix(matrix1, matrix2):
    # matrix1 * matrix2
    row1 = len(matrix1)
    col2 = len(matrix2[0])
    row2 = len(matrix2)
    temp = [[0] * row1 for _ in range(col2)]

    for i in range(row1):
        for j in range(col2):
            for k in range(row2):
                temp[i][j] += matrix1[i][k] * matrix2[k][j]

    return temp


def power(matrix, b):
    if b == 1:
        for i in range(n):
            for j in range(n):
                matrix[i][j] %= 1000

        return matrix

    temp = power(matrix, b // 2)
    temp = multiple_matrix(temp, temp)

    # 거듭제곱이 홀수인 경우
    if b % 2 != 0:
        temp = multiple_matrix(temp, matrix_A)  # 홀수인 경우 원본 행렬을 한번 더 곱해야함.

    for i in range(n):
        for j in range(n):
            temp[i][j] %= 1000

    return temp


n, b = map(int, input().split())  # n차 정사각행렬, b거듭제곡
matrix_A = [list(map(int, input().split())) for _ in range(n)]  # 원본 행렬

rst = power(matrix_A, b)
for i in range(n):
    for j in range(n):
        print(rst[i][j], end=" ")
    print()


"""
39. 10830 행렬 제곱 (Gold 4)
    - 1629 곱셈 문제와 같은 분할정복 문제 근데 이제.. 행렬곱을 곁들인
      거듭제곱 성질을 이용해서 계속 A^b를 (A^b//2)^2 형태로 분할해간다. 당연히 홀수일때는 따로 처리한다. 
      
      이렇게 분할을 통해서 n-1번이 아니라 log시간으로 풀이할 수 있다. 
    
    - 행렬의 곱셈은 예를 들어 행렬 A와 B의 곱 AB라고 하면 A의 열길이와 B의 행길이가 일치해야 할 수 있다.
      때문에 행렬 곱을 보면 i, j, j, k의 곱으로 표현할 수 있다. 

      당연하게 행렬에서는 AB != BA가 아니다. 

    - 처음에 한번 틀렸었는데, b==1일때, 모든 원소 값이 1000이 들어왔을때, 나머지를 구하지 않고 출력해서 틀렸었다. 
"""