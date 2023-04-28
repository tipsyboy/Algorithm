# https://www.acmicpc.net/problem/13565

# 1_dfs_stack
import sys

input = sys.stdin.readline
directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]


def dfs_stack(start: tuple) -> bool:
    stack = [start]

    while stack:
        x, y = stack.pop()

        if visited[x][y]:
            continue

        if x == M - 1:
            return True

        visited[x][y] = True
        for i in range(4):
            nx, ny = x + directions[i][0], y + directions[i][1]

            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue

            if visited[nx][ny] or grid[nx][ny] == 1:
                continue

            stack.append((nx, ny))

    return False


M, N = map(int, input().split())
grid = [list(map(int, input().rstrip())) for _ in range(M)]
visited = [[False] * N for _ in range(M)]

ans = "NO"
for i in range(N):
    if grid[0][i] == 0:
        if dfs_stack((0, i)):
            ans = "YES"
            break
print(ans)

# 2_dfs
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]


def dfs(now: tuple) -> None:
    x, y = now

    if x == M - 1:
        print("YES")
        exit()

    visited[x][y] = True
    for i in range(4):
        nx, ny = x + directions[i][0], y + directions[i][1]

        if nx < 0 or nx >= M or ny < 0 or ny >= N:
            continue

        if visited[nx][ny] or grid[nx][ny] == 1:
            continue

        dfs((nx, ny))


M, N = map(int, input().split())
grid = [list(map(int, input().rstrip())) for _ in range(M)]
visited = [[False] * N for _ in range(M)]

for i in range(N):
    if grid[0][i] == 0:
        dfs((0, i))

print("NO")


# 3_bfs
import sys
from collections import deque

input = sys.stdin.readline
directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]


def bfs(start: list) -> bool:
    q = deque(start)

    while q:
        x, y = q.popleft()

        if x == M - 1:
            return True

        for i in range(4):
            nx, ny = x + directions[i][0], y + directions[i][1]

            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            if visited[nx][ny] or grid[nx][ny] == 1:
                continue

            q.append((nx, ny))
            visited[nx][ny] = True

    return False


M, N = map(int, input().split())
grid = [list(map(int, input().rstrip())) for _ in range(M)]
visited = [[False] * N for _ in range(M)]

start = []
for i in range(N):
    if grid[0][i] == 0:
        start.append((0, i))
        visited[0][i] = True
print("YES" if bfs(start) else "NO")



"""
13565. 침투
    - 실버에 시간 너무씀 걍 bfs로 때리는게 나았을듯
"""