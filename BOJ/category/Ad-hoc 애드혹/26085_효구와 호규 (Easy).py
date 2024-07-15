# 2024.07.09 TUE
# https://www.acmicpc.net/problem/26085

import sys

input = sys.stdin.readline


def is_zero_one_even(grid):
    zero = 0
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 0:
                zero += 1

    return not (zero & 1) and not ((N * M - zero) & 1)


def can_move(grid):
    for i in range(N - 1):
        for j in range(M - 1):
            if grid[i][j] == grid[i + 1][j] or grid[i][j] == grid[i][j + 1]:
                return True
    return False


N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

if is_zero_one_even(grid) and can_move(grid):
    print(1)
else:
    print(-1)
