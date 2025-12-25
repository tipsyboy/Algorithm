# https://www.acmicpc.net/problem/2980

import sys

input = sys.stdin.readline

N, L = map(int, input().split())
W = 0  # 기다린 시간
for _ in range(N):
    D, R, G = map(int, input().split())

    r = (D + W) % (R + G)

    if r < R:
        W += R - r
print(W + L)
