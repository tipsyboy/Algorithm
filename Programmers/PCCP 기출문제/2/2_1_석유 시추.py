# https://school.programmers.co.kr/learn/courses/30/lessons/250136

from collections import deque

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def solution(land):
    def bfs(sx, sy, idx):
        q = deque([(sx, sy)])
        visited[sx][sy][0], visited[sx][sy][1] = 1, idx
        oil = [(sx, sy)]

        cnt = 1
        while q:
            x, y = q.popleft()

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if visited[nx][ny][0] != -1 or land[nx][ny] == 0:
                    continue
                visited[nx][ny][0], visited[nx][ny][1] = 1, idx

                q.append((nx, ny))
                oil.append((nx, ny))
                cnt += 1

        for x, y in oil:
            visited[x][y][0] = cnt

    n, m = len(land), len(land[0])
    visited = [[[-1] * 2 for _ in range(m)] for __ in range(n)]
    idx = 0
    for i in range(n):
        for j in range(m):
            if land[i][j] == 0 or visited[i][j][0] != -1:
                continue
            bfs(i, j, idx)
            idx += 1

    ans = -1
    for j in range(m):
        cnt = 0
        worked = set()
        for i in range(n):
            if land[i][j] == 0 or visited[i][j][1] in worked:
                continue
            cnt += visited[i][j][0]
            worked.add(visited[i][j][1])
        ans = max(ans, cnt)

    return ans
