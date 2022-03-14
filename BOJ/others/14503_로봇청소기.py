import sys

input = sys.stdin.readline


def solution(y, x, direction):
    # 북 동 남 서
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    visited = [[False] * m for _ in range(n)]
    rst = 0

    while True:
        # 현재 위치가 청소가 되지 않은 곳이면 청소 갈김
        if not visited[y][x]:
            visited[y][x] = True
            rst += 1

        flag = False
        for i in range(1, 5):
            nd = (direction + 3 * i) % 4
            ny = y + dy[nd]
            nx = x + dx[nd]
            if 0 <= ny < n and 0 <= nx < m and graph[ny][nx] != 1:
                if not visited[ny][nx]:
                    y, x, direction = ny, nx, nd
                    flag = True
                    break

        if not flag:
            nd = (direction + 2) % 4
            ny = y + dy[nd]
            nx = x + dx[nd]

            if 0 <= ny < n and 0 <= nx < m and graph[ny][nx] != 1:
                y, x = ny, nx
            else:
                break

    return rst


n, m = map(int, input().split())
y, x, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
print(solution(y, x, d))
