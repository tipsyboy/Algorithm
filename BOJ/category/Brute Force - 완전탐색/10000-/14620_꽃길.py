# 2024.06.13 SAT
# https://www.acmicpc.net/problem/14620

import sys

input = sys.stdin.readline
directions = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]


def bt(depth, cost):
    global ans

    if depth == 3:
        ans = min(ans, cost)
        return

    for i in range(1, N - 1):
        for j in range(1, N - 1):
            if can_seed(i, j):
                this_cost = get_pos_cost(i, j)
                seed(i, j, True)
                bt(depth + 1, cost + this_cost)
                seed(i, j, False)


def get_pos_cost(x, y):
    cost = 0
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        cost += grid[nx][ny]
    return cost


def seed(x, y, s):
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        vis[nx][ny] = s


def can_seed(x, y):
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if vis[nx][ny]:
            return False

    return True


N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
vis = [[False] * N for _ in range(N)]
ans = float("inf")

bt(0, 0)
print(ans)
