import sys
from collections import deque

input = sys.stdin.readline


def bfs(x, y):
    dx = [0, -1, -1, -1, 0, 1, 1, 1]
    dy = [-1, -1, 0, 1, 1, 1, 0, -1]

    q = deque([(x, y)])
    graph[x][y] = 0

    while q:
        x, y = q.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < row and 0 <= ny < col and graph[nx][ny] == 1:
                q.append((nx, ny))
                graph[nx][ny] = 0


while True:
    col, row = map(int, input().split())

    if row == 0 and col == 0:
        break
    
    graph = [list(map(int, input().split())) for _ in range(row)]
    count = 0

    for i in range(row):
        for j in range(col):
            if graph[i][j] == 1:
                bfs(i, j)
                count += 1

    print(count)
