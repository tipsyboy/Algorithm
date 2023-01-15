# https://www.acmicpc.net/problem/2589

import sys
from collections import deque

input = sys.stdin.readline
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(sx: int, sy: int) -> int:
    q = deque([(sx, sy)])
    visited = [[-1] * M for _ in range(N)]
    visited[sx][sy] = 0

    longest = 0
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + directions[i][0], y + directions[i][1]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if graph[nx][ny] == "W" or visited[nx][ny] != -1:
                continue

            q.append((nx, ny))
            visited[nx][ny] = visited[x][y] + 1
            longest = max(longest, visited[nx][ny])

    return longest


N, M = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(N)]

ans = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == "W":
            continue
        ans = max(ans, bfs(i, j))
print(ans)


"""
2589. 보물섬
    - 단순 BFS에다가 N, M의 범위가 50까지로 완전 탐색해서 해결하였다. 
    
    - but, 파이썬에서는 왜 통과가 안되는지 모르겠음.. 
      O((NM)^2)로 계산했고, N, M의 범위가 50이면 아무리 파이썬이라도 추가시간 없이도 통과해야 되는 거 아닌가?
      일단 질문은 올렸는데.. 답이 안달린다
"""