# p(6)부터 규칙성을 갖는 삼각형을 만들어 낸다.
# 따라서 DP
import sys


def tri_helix(n):
    if len(triangle_len) >= n:
        return triangle_len[n-1]

    for j in range(len(triangle_len), n):
        triangle_len.append(triangle_len[j-1] + triangle_len[j-5])

    return triangle_len[n-1]


test_case = int(sys.stdin.readline())
triangle_len = [1, 1, 1, 2, 2]  # 6번째 부터 규칙성을 띔.

for i in range(test_case):
    n = int(sys.stdin.readline())

    print(tri_helix(n))
