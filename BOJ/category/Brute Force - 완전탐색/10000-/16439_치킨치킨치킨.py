# 2025.02.15 SAT
# https://www.acmicpc.net/problem/16439

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
favorites = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for a in range(M - 2):
    for b in range(a + 1, M - 1):
        for c in range(b + 1, M):
            temp = 0
            for i in range(N):
                temp += max(favorites[i][a], favorites[i][b], favorites[i][c])

            ans = max(ans, temp)
print(ans)
