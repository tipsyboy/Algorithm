
# # 1)
# import sys

# n = int(sys.stdin.readline())
# int_triangle = []

# for i in range(n):
#     int_triangle.append(list(map(int, sys.stdin.readline().split())))

# result = int_triangle[0]  # 결과 창 - for를 돌때는 이전 항.

# for i in range(1, n):
#     feature_map = int_triangle[i]
#     temp = []

#     for idx, elem in enumerate(feature_map):
#         if idx == 0:
#             temp.append(elem + result[0])
#         elif idx == len(feature_map) - 1:
#             temp.append(elem + result[idx-1])
#         else:
#             temp.append(elem + max(result[idx-1], result[idx]))

#     result = temp

# print(max(result))

##################################################################################

# # 2)
# import sys

# n = int(sys.stdin.readline())
# triangle = []

# for i in range(n):
#     triangle.append(list(map(int, sys.stdin.readline().split())))

# for i in range(1, n):
#     for j in range(len(triangle[i])):
#         if j == 0:
#             triangle[i][j] += triangle[i-1][j]
#         elif j == len(triangle[i]) - 1:
#             triangle[i][j] += triangle[i-1][j-1]
#         else:
#             triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])

# print(max(triangle[-1]))


# ?? 1, 2를 비교했을 때, 1이 더 메모리도 많이 사용하고 시간도 더 걸릴줄 알았는데,
# 반대의 결과가 나와서 의외다.
# 왜 그러지
