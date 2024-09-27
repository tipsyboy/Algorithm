# 2024.09.23 MON
# https://www.acmicpc.net/problem/30412

import sys

input = sys.stdin.readline


def solution(N, X, A):
    if abs(A[0] - A[1]) >= X or abs(A[N - 1] - A[N - 2]) >= X:
        return 0

    ans = X - max(abs(A[0] - A[1]), abs(A[N - 1] - A[N - 2]))

    for i in range(1, N - 1):
        # 1. < <
        d1 = max(0, A[i - 1] + X - A[i])
        d2 = max(0, A[i] + d1 + X - A[i + 1])
        v1 = d1 + d2

        # 2. < >
        v2 = max(0, max(A[i - 1], A[i + 1]) + X - A[i])

        # 3. > <
        d1 = max(0, A[i] + X - A[i - 1])
        d2 = max(0, A[i] + X - A[i + 1])
        v3 = d1 + d2

        # 4. > >
        d1 = max(0, A[i + 1] + X - A[i])
        d2 = max(0, A[i] + d1 + X - A[i - 1])
        v4 = d1 + d2

        ans = min(ans, v1, v2, v3, v4)

    return ans


N, X = map(int, input().split())
A = list(map(int, input().split()))

print(solution(N, X, A))
