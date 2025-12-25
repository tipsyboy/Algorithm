# 2024.01.02 THU
# https://www.acmicpc.net/problem/25644

import sys

input = sys.stdin.readline
INF = float("inf")


N = int(input())
A = list(map(int, input().split()))

mn = INF
ans = 0
for i in range(N):
    ans = max(ans, A[i] - mn)
    if A[i] < mn:
        mn = A[i]

print(ans)
