# 2024.10.28 MON
# https://www.acmicpc.net/problem/17357

import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

P = [0]
P2 = [0]
for i in range(N):
    P.append(P[-1] + A[i])
    P2.append(P2[-1] + A[i] ** 2)

for k in range(1, N + 1):
    rst = -1
    value = -1
    for i in range(1, N - k + 2):
        km = P[i + k - 1] - P[i - 1]
        kkV = (P2[i + k - 1] - P2[i - 1]) * k - (km**2)
        if value < kkV:
            value = kkV
            rst = i

    print(rst)
