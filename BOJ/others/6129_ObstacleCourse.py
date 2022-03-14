import sys
from heapq import heappush, heappop

input = sys.stdin.readline
INF = int(1e9)


def find_pos(graph, char):
    for i in range(len(graph)):
        for j in range(len(graph)):
            if graph[i][j] == char:
                return i, j


def bfs(graph):
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    sy, sx = find_pos(graph, "A")
    des_y, des_x = find_pos(graph, "B")

    pq = []
    rst = [[INF] * n for _ in range(n)]
    heappush(pq, (-1, sy, sx, 4))

    while pq:
        rot, y, x, direction = heappop(pq)

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < n and graph[ny][nx] != "x":
                if rst[ny][nx] <= rot:
                    continue

                if direction == i:
                    rst[ny][nx] = rot
                    heappush(pq, (rot, ny, nx, direction))
                else:
                    rst[ny][nx] = rot + 1
                    heappush(pq, (rot + 1, ny, nx, i))

    return rst[des_y][des_x]


n = int(input())
graph = [list(input().rstrip()) for _ in range(n)]
print(bfs(graph))