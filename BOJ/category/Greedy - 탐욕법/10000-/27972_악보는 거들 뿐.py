# 2024.09.26 THU
# https://www.acmicpc.net/problem/27972

import sys

input = sys.stdin.readline

M = int(input())
P = list(map(int, input().split()))

up = [1] * M
for i in range(1, M):
    if P[i] > P[i - 1]:
        up[i] = up[i - 1] + 1
    elif P[i] == P[i - 1]:
        up[i] = up[i - 1]

down = [1] * M
for i in range(1, M):
    if P[i] < P[i - 1]:
        down[i] = down[i - 1] + 1
    elif P[i] == P[i - 1]:
        down[i] = down[i - 1]

print(max(max(up), max(down)))
