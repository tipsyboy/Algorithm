# 2024.09.04 WED
# https://www.acmicpc.net/problem/27890

import sys

input = sys.stdin.readline

X, N = map(int, input().split())

for _ in range(N):
    if X & 1:
        X = (2 * X) ^ 6
    else:
        X = (X // 2) ^ 6

print(X)
