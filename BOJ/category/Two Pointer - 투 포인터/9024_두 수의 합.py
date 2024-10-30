# 2024.10.24 THU
# https://www.acmicpc.net/problem/9024

import sys

input = sys.stdin.readline
INF = float("inf")

t = int(input())
ans = []
for _ in range(t):
    n, K = map(int, input().split())
    arr = list(map(int, input().split()))

    arr.sort()

    lo, hi = 0, n - 1
    minv = INF
    cnt = 0
    while lo < hi:
        sumv = arr[lo] + arr[hi]
        diff = K - sumv

        if abs(diff) < minv:
            cnt = 1
            minv = abs(diff)
        elif abs(diff) == minv:
            cnt += 1

        if diff < 0:
            hi -= 1
        elif diff > 0:
            lo += 1
        else:
            lo += 1
            hi -= 1

    ans.append(cnt)

print(*ans, sep="\n")
