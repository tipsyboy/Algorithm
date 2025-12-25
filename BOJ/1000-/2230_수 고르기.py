# https://www.acmicpc.net/problem/2230

import sys
from bisect import bisect_left

input = sys.stdin.readline
INF = float("inf")


def bi(A: list, N: int, M: int) -> int:
    """
    Ai - Aj >= M
    Aj + M <= Ai
    """

    A.sort()
    ans = INF
    for i in range(N):
        t = M + A[i]

        left = bisect_left(A, t)
        if left >= N:
            continue
        ans = min(ans, A[left] - A[i])

    return ans


def tp(A: list, N: int, M: int) -> int:
    A.sort()

    lo, hi = 0, 0
    ans = INF
    while hi < N and lo < N:
        while hi < N and A[hi] - A[lo] < M:
            hi += 1

        if hi == N:
            break
        ans = min(ans, A[hi] - A[lo])

        while lo < N and A[hi] - A[lo] >= M:
            ans = min(ans, A[hi] - A[lo])
            lo += 1

    return ans


def tp2(A: list, N: int, M: int) -> int:
    A.sort()

    hi, ans = 0, INF
    for lo in range(N):
        while hi < N and A[hi] - A[lo] < M:
            hi += 1
        if hi == N:
            break
        ans = min(ans, A[hi] - A[lo])
    return ans


N, M = map(int, input().split())
A = []
for _ in range(N):
    A.append(int(input()))

# print(bi(A, N, M))
# print(tp(A, N, M))
print(tp2(A, N, M))