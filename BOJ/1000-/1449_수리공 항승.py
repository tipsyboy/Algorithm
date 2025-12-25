# 2025.02.14 FRI
# https://www.acmicpc.net/problem/1449

import sys

input = sys.stdin.readline

N, L = map(int, input().split())
burst = sorted(map(int, input().split()))

x = 0
cnt = 0
for i in range(N):
    if burst[i] - 0.5 >= x:
        cnt += 1
        x = burst[i] - 0.5 + L
print(cnt)
