# # 1) 정사각행렬의 경우
# def rotate_a_matrix_90_degree(matrix):
#     n = len(matrix)  # 정사각행렬의 길이
#     rst_matrix = [[0] * n for _ in range(n)]  # rst = [[0] * n * n] 으로 쓰지 않는 이유

#     for row in range(n):
#         for col in range(n):
#             rst_matrix[col][n-row-1] = matrix[row][col]

#     print(rst_matrix)


# 2) 정사각행렬이 아닌 경우(x) -> 모든 경우에 대해서 일반화
def rotate_a_matrix_90_degree(matrix):
    row_len = len(matrix)  # 현재 행 길이
    col_len = len(matrix[0])  # 현재 열 길이

    # 여기서 정사각행렬이 아닌경우에는 행과 열이 뒤바뀌기 때문에 결과배열을 바꿔서 생성함
    rst_matrix = [[0] * row_len for _ in range(col_len)]

    # 회전한 배열의 값을 배치
    for row in range(row_len):
        for col in range(col_len):
            rst_matrix[col][row_len - row - 1] = matrix[row][col]

    return rst_matrix


mat = [[1, 2, 3], [4, 5, 6]]
rotate_a_matrix_90_degree(mat)
