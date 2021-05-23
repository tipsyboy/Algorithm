import sys
from collections import deque
input = sys.stdin.readline


# 미로 찾기
def bfs(start_row, start_col):
    rst = 1
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    q = deque()
    q.append((start_row, start_col))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < row and 0 <= ny < col:
                if graph[nx][ny] == 1:
                    q.append((nx, ny))
                    graph[nx][ny] = graph[x][y] + 1

    return graph[row-1][col-1]


row, col = map(int, input().split())
graph = [list(map(int, str(input().rstrip()))) for _ in range(row)]

print(bfs(0, 0))
