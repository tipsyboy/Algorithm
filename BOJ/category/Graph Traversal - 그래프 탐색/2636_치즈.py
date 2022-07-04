import sys
from collections import deque

input = sys.stdin.readline
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def get_surface(n: int, m: int) -> list:
    q = deque([(0, 0)])
    surface = [[False] * m for _ in range(n)]
    surface[0][0] = True

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + DIRECTIONS[i][0], y + DIRECTIONS[i][1]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if surface[nx][ny] or graph[nx][ny] == 1:
                continue

            surface[nx][ny] = True
            q.append((nx, ny))

    return surface


def melting(surface: list, cheese: int) -> int:
    for x in range(n):
        for y in range(m):
            if graph[x][y] == 0:
                continue

            for i in range(4):
                nx, ny = x + DIRECTIONS[i][0], y + DIRECTIONS[i][1]
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue

                if surface[nx][ny]:
                    cheese -= 1
                    graph[x][y] = 0
                    break

    return cheese


n, m = map(int, input().split())  # row, col
graph = [list(map(int, input().split())) for _ in range(n)]
cheese = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            cheese += 1

time = 0
prev = cheese
while True:
    surface = get_surface(n, m)
    cheese = melting(surface, cheese)
    time += 1
    if cheese == 0:
        break
    prev = cheese

print(time)
print(prev)


"""
2636. 치즈
    - 가벼운 bfs + 치즈가 아닌 바깥 공기를 탐색
"""