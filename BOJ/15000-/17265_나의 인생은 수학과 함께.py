# https://www.acmicpc.net/problem/17265

"""
17265. 나의 인생은 수학과 함께
    - 꽤나 귀찮은 문제였음. 괜히 반복문 구현하려다가 더 어지러워짐
    - 앞으로도 dfs는 반복문 구현보다 그냥 재귀구현이 더 편할거같다.
"""

import sys

input = sys.stdin.readline
INF = float("inf")
directions = [(1, 0), (0, 1)]


def cal(a: int, b: int, op: str) -> int:
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b


def OOB(nx: int, ny: int) -> bool:
    if nx < 0 or nx >= N or ny < 0 or ny >= N:
        return True
    return False


def dfs(x: int, y: int, v: int, op: str) -> None:
    global maxv, minv

    visited[x][y] = True

    if grid[x][y].isnumeric():
        v = cal(v, int(grid[x][y]), op)
    else:
        op = grid[x][y]

    for i in range(2):
        nx, ny = x + directions[i][0], y + directions[i][1]

        if OOB(nx, ny) or visited[nx][ny]:
            continue
        dfs(nx, ny, v, op)

    if x == N - 1 and y == N - 1:
        maxv = max(maxv, v)
        minv = min(minv, v)

    visited[x][y] = False


N = int(input())
grid = [list(input().split()) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

maxv, minv = -INF, INF
dfs(0, 0, 0, "+")
print(maxv, minv)
