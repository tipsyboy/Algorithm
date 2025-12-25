# 2025.02.20 THU
# https://www.acmicpc.net/problem/27648

import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())

if K < N + M - 1:
    print("NO")
else:
    print("YES")
    for i in range(N):
        print(*[j for j in range(i + 1, i + M + 1)])
