import sys
from collections import deque

input = sys.stdin.readline
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
COL = 10


def bfs(sx, sy, color) -> set:
    q = deque([(sx, sy)])
    visited = set()
    visited.add((sx, sy))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + directions[i][0], y + directions[i][1]

            if nx < 0 or nx >= N or ny < 0 or ny >= COL:
                continue
            if color != graph[nx][ny] or (nx, ny) in visited:
                continue

            q.append((nx, ny))
            visited.add((nx, ny))

    return visited


def drop_block() -> None:
    for i in range(COL):
        q = deque()
        for j in range(N - 1, -1, -1):
            if graph[j][i] == 0:
                q.append(j)
            elif graph[j][i] != 0 and q:
                drop_loc = q.popleft()
                graph[drop_loc][i] = graph[j][i]
                graph[j][i] = 0
                q.append(j)


def break_block(vis) -> None:
    for x, y in vis:
        graph[x][y] = 0


def Mooyo_Mooyo():
    while True:
        flag = False
        for i in range(N):
            for j in range(COL):
                if graph[i][j] == 0:
                    continue
                vis = bfs(i, j, graph[i][j])
                if len(vis) >= K:
                    break_block(vis)
                    flag = True

        if not flag:
            break
        drop_block()


N, K = map(int, input().split())  # row, 최소 파괴 개수
graph = [list(map(int, input().rstrip())) for _ in range(N)]
Mooyo_Mooyo()

for i in range(N):
    print(*graph[i], sep="")


"""
16768. Mooyo Mooyo
    - bfs + 구현
"""