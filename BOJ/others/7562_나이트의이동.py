import sys
from collections import deque

input = sys.stdin.readline


def bfs(n, graph):
    sy, sx = map(int, input().split())
    dest_y, dest_x = map(int, input().split())

    dy = [-2, -2, -1, 1, 2, 2, 1, -1]
    dx = [-1, 1, 2, 2, 1, -1, -2, -2]
    q = deque([(sy, sx)])

    while q:
        y, x = q.popleft()

        if y == dest_y and x == dest_x:
            return graph[dest_y][dest_x]

        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < n and graph[ny][nx] == 0:
                graph[ny][nx] = graph[y][x] + 1
                q.append((ny, nx))

    return graph[dest_y][dest_x]


tc = int(input())

for _ in range(tc):
    n = int(input())
    graph = [[0] * n for _ in range(n)]
    print(bfs(n, graph))