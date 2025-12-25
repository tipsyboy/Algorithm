# https://www.acmicpc.net/problem/2447

import sys

input = sys.stdin.readline


def print_star(now: int, x: int, y: int) -> None:
    if now == 1:
        grid[x][y] = "*"
        return

    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            print_star(now // 3, x + now // 3 * i, y + now // 3 * j)


N = int(input())
grid = [[" " for _ in range(N)] for __ in range(N)]
print_star(N, 0, 0)
for i in range(N):
    print("".join(grid[i]))