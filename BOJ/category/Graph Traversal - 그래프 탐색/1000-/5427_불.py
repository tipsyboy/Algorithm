# https://www.acmicpc.net/problem/5427

import sys
from collections import deque

input = sys.stdin.readline
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def move_fire(fire: deque) -> None:
    for _ in range(len(fire)):
        x, y = fire.popleft()

        for i in range(4):
            nx, ny = x + directions[i][0], y + directions[i][1]

            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue
            if graph[nx][ny] != ".":
                continue

            graph[nx][ny] = "*"
            fire.append((nx, ny))


def bfs(graph: list) -> int:
    q = deque()
    fire = deque()
    visited = [[False] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if graph[i][j] == "*":
                fire.append((i, j))
            if graph[i][j] == "@":
                q.append((i, j))
                visited[i][j] = True
                graph[i][j] = "."

    move = 0
    while q:
        move += 1
        move_fire(fire)
        for _ in range(len(q)):
            x, y = q.popleft()

            for i in range(4):
                nx, ny = x + directions[i][0], y + directions[i][1]

                if nx < 0 or nx >= h or ny < 0 or ny >= w:
                    return move
                if graph[nx][ny] == "#" or graph[nx][ny] == "*" or visited[nx][ny]:
                    continue

                visited[nx][ny] = True
                q.append((nx, ny))

    return -1


TC = int(input())
for _ in range(TC):
    w, h = map(int, input().split())
    graph = [list(input().rstrip()) for _ in range(h)]

    rst = bfs(graph)
    print(rst) if rst != -1 else print("IMPOSSIBLE")


"""
5427. 불
    - bfs, 시뮬레이션 문제

    - 포인트는 불이 번질 곳에는 이동하지 못하는 것 이므로 
      이 문장으로 불이 먼저 번지고 이동 하면 된다는 것을 알 수 있음.

    - 위의 조건에 맞게 시뮬레이션 하고 맵을 벗어나면 탈출 한 것으로 간주하고 리턴한다.
"""