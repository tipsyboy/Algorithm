import sys
from collections import deque

input = sys.stdin.readline
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(sx: int, sy: int, grid: list, visited: list) -> int:
    q = deque([(sx, sy)])
    visited[sx][sy] = True
    cnt = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + directions[i][0], y + directions[i][1]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if visited[nx][ny] or grid[nx][ny] == 0:
                continue

            q.append((nx, ny))
            visited[nx][ny] = True
            cnt += 1

    return cnt


N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

ans = [0, 0]
visited = [[False] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if grid[i][j] == 0 or visited[i][j]:
            continue
        ans[1] = max(ans[1], bfs(i, j, grid, visited))
        ans[0] += 1

print(*ans, sep="\n")


"""
1926. 그림
    - 그냥 그래프 탐색
"""