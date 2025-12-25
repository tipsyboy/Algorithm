# 2025.01.06 MON
# https://www.acmicpc.net/problem/9657

import sys

input = sys.stdin.readline

N = int(input())
d = [1, 0, 1, 1] + [0] * (N - 4)  # 승패승승
# 상근->창영 순서
for i in range(4, N):
    if d[i - 1] == 0 or d[i - 3] == 0 or d[i - 4] == 0:
        d[i] = 1
print("SK") if d[N - 1] else print("CY")
