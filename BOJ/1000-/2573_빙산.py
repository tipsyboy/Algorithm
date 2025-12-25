import sys
from collections import deque

input = sys.stdin.readline
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def melt(glaciers) -> set:
    temp = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if not graph[i][j]:
                continue

            cnt = 0
            for d in range(4):
                nx, ny = i + directions[d][0], j + directions[d][1]
                if graph[nx][ny] == 0:
                    cnt += 1
            temp[i][j] = cnt

    for i in range(N):
        for j in range(M):
            if not graph[i][j]:
                continue

            g_val = graph[i][j] - temp[i][j]
            if g_val <= 0:
                graph[i][j] = 0
                glaciers.remove((i, j))
            else:
                graph[i][j] = g_val

    return glaciers


def get_glaciers() -> set:
    glaciers = set()

    for i in range(N):
        for j in range(M):
            if graph[i][j]:
                glaciers.add((i, j))

    return glaciers


def check(sx, sy) -> int:
    q = deque([(sx, sy)])
    visited = [[False] * M for _ in range(N)]
    visited[sx][sy] = True
    cnt = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + directions[i][0], y + directions[i][1]

            if nx < 0 or nx >= N or ny < 0 or ny >= M or visited[nx][ny]:
                continue

            if not graph[nx][ny]:
                continue

            visited[nx][ny] = True
            q.append((nx, ny))
            cnt += 1

    return cnt


N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
glaciers = get_glaciers()
year = 1

while True:
    glaciers = melt(glaciers)
    if len(glaciers) == 0:
        year = 0
        break

    sx, sy = list(glaciers)[0]
    if len(glaciers) != check(sx, sy):
        break
    year += 1

print(year)


"""
    2573. 빙산

    - pypy3 제출

    - 처음에 빙하의 위치를 저장하고 시간이 지남에 따라서 빙하를 지워줌
    - 빙하가 쪼개지기 전에 빙하의 개수가 0이 되면 break 
    - 빙하가 쪼개지면 break

    - 빙하가 녹을때는 현재 상태에서 녹아야하므로 temp로 녹는 정도를 따로 저장해서 한꺼번에 처리함
"""