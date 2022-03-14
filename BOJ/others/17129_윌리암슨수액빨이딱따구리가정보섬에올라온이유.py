import sys
from collections import deque

input = sys.stdin.readline


def get_start(graph, target):
    for i in range(n):
        for j in range(m):
            if graph[i][j] == target:
                return (i, j)


def bfs(sy, sx):
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    q = deque([(sy, sx, 0)])

    while q:
        y, x, cnt = q.popleft()

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]

            if 0 <= ny < n and 0 <= nx < m and graph[ny][nx] != 1:
                if graph[ny][nx] > 2:
                    return cnt + 1

                q.append((ny, nx, cnt + 1))
                graph[ny][nx] = 1

    return -1


n, m = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
sy, sx = get_start(graph, 2)
rst = bfs(sy, sx)

if rst != -1:
    print("TAK")
    print(rst)
else:
    print("NIE")
