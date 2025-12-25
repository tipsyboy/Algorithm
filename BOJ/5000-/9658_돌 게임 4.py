# 2025.01.07 TUE
# https://www.acmicpc.net/problem/9658

import sys

input = sys.stdin.readline

N = int(input())
d = [0, 1, 0, 1] + [0] * (N - 4)
for i in range(4, N):
    d[i] = 1 if d[i - 1] == 0 or d[i - 3] == 0 or d[i - 4] == 0 else 0
print("SK") if d[N - 1] else print("CY")
