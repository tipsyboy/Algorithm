# 2025.01.23 THU
# https://www.acmicpc.net/problem/1915

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(map(int, input().rstrip())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if i == 0 or j == 0 or grid[i][j] == 0:
            continue

        if grid[i - 1][j] and grid[i][j - 1] and grid[i - 1][j - 1]:
            grid[i][j] = min(grid[i - 1][j], grid[i][j - 1], grid[i - 1][j - 1]) + 1

ans = 0
for i in range(n):
    for j in range(m):
        ans = max(ans, grid[i][j])

print(ans * ans)
