# https://www.acmicpc.net/problem/2799

import sys

input = sys.stdin.readline

M, N = map(int, input().split())
APT = [list(input().rstrip()) for _ in range(5 * M + 1)]

ans = [0] * 5
for i in range(1, 5 * M + 1, 5):
    for j in range(1, 5 * N + 1, 5):
        for k in range(5):
            if APT[i + k][j] != "*":
                ans[k] += 1
                break

print(*ans)
