# https://www.acmicpc.net/problem/2217

import sys

input = sys.stdin.readline

N = int(input())
ropes = []
for _ in range(N):
    ropes.append(int(input()))

ropes.sort(reverse=True)

maxv = ropes[0]
for i in range(1, N):
    if ropes[i] * (i + 1) > maxv:
        maxv = ropes[i] * (i + 1)

print(maxv)