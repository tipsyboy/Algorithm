# https://school.programmers.co.kr/learn/courses/30/lessons/250136

from collections import deque


def solution(land):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def bfs(sx, sy):
        q = deque([(sx, sy)])
        visited[sx][sy] = True
        points = set()
        cnt = 1
        while q:
            x, y = q.popleft()

            points.add(y)

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if visited[nx][ny] or land[nx][ny] == 0:
                    continue
                q.append((nx, ny))
                visited[nx][ny] = True
                cnt += 1

        for point in points:
            oil[point] += cnt

    n, m = len(land), len(land[0])
    visited = [[False] * m for _ in range(n)]
    oil = [0] * m
    for i in range(n):
        for j in range(m):
            if land[i][j] == 0 or visited[i][j]:
                continue
            bfs(i, j)

    return max(oil)
