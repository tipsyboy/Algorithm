import sys
from collections import deque

input = sys.stdin.readline
directions = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]


def BFS(sy, sx):
    visited = [[0] * N for _ in range(N)]
    q = deque([(sy, sx, 0)])
    visited[sy][sx] = 0

    while q:
        y, x, move = q.popleft()

        for i in range(8):
            ny, nx = y + directions[i][0], x + directions[i][1]

            if ny < 0 or ny >= N or nx < 0 or nx >= N or visited[ny][nx]:
                continue

            visited[ny][nx] = move + 1
            q.append((ny, nx, move + 1))

    return visited


N, M = map(int, input().split())
enemies = []
y, x = map(int, input().split())

visited = BFS(y - 1, x - 1)
# print(*visited, sep="\n")
answer = []
for _ in range(M):
    r, c = map(int, input().split())
    answer.append(visited[r - 1][c - 1])

print(*answer)


"""
    - 전형적인 BFS
    - 시간 복잡도 줄이기 위해서 모든 위치의 값을 구해둔 뒤에 쿼리가 들어오면 바로바로 해결
"""