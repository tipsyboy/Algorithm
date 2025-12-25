# https://www.acmicpc.net/problem/5541

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
grid = [[0] * (N + 2) for _ in range(N + 2)]

for _ in range(M):
    A, B, X = map(int, input().split())

    grid[A - 1][B - 1] += 1
    grid[A - 1][B] -= 1

    grid[A + X][B - 1] -= 1
    grid[A + X + 1][B] += 1

    grid[A + X][B + X + 1] += 1
    grid[A + X + 1][B + X + 1] -= 1

for i in range(N):
    for j in range(1, N):
        grid[i][j] += grid[i][j - 1]

for i in range(N):
    for j in range(1, N):
        grid[j][i] += grid[j - 1][i]

for i in range(N):
    x, y = i + 1, 1
    while x < N + 2:
        grid[x][y] += grid[x - 1][y - 1]
        x += 1
        y += 1

ans = 0
for i in range(N):
    for j in range(i + 1):
        if grid[i][j]:
            ans += 1
print(ans)


"""
5541. 釘 (Nails)
    - imos 연습
"""