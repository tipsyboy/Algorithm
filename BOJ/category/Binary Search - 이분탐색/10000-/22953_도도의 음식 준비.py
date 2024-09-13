# 2024.09.05 THU
# https://www.acmicpc.net/problem/22953

import sys
from itertools import combinations_with_replacement

input = sys.stdin.readline

N, K, C = map(int, input().split())
A = list(map(int, input().split()))


def bs(lo, hi, temp):

    while lo <= hi:
        mid = (lo + hi) // 2

        cnt = 0
        for i in range(N):
            cnt += mid // temp[i]

        if cnt >= K:
            hi = mid - 1
        else:
            lo = mid + 1

    return lo


ans = float("inf")
for buff in combinations_with_replacement(range(N), C):
    temp = [0] * N
    for i in range(N):
        temp[i] = A[i]

    for b in buff:
        if temp[b] < 2:
            continue
        temp[b] -= 1

    ans = min(ans, bs(1, max(temp) * K, temp))

print(ans)
