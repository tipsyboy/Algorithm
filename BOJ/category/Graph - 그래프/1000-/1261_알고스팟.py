import sys
from collections import deque
from heapq import heappush, heappop

input = sys.stdin.readline
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
INF = float("inf")


def bfs(sx: int, sy: int) -> int:
    q = deque([(sx, sy)])
    visited = [[INF] * M for _ in range(N)]
    visited[sx][sy] = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + directions[i][0], y + directions[i][1]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if graph[nx][ny] == 0 and visited[nx][ny] > visited[x][y]:
                q.appendleft((nx, ny))
                visited[nx][ny] = visited[x][y]
            elif graph[nx][ny] == 1 and visited[nx][ny] > visited[x][y] + 1:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1

    return visited[N - 1][M - 1]


def dijkstra(sx: int, sy: int) -> int:
    pq = []
    heappush(pq, (0, sx, sy))
    visited = [[INF] * M for _ in range(N)]
    visited[sx][sy] = 0

    while pq:
        now_cost, x, y = heappop(pq)

        if now_cost > visited[x][y]:
            continue

        for i in range(4):
            nx, ny = x + directions[i][0], y + directions[i][1]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            cost = now_cost + graph[nx][ny]
            if cost < visited[nx][ny]:
                visited[nx][ny] = cost
                heappush(pq, (cost, nx, ny))

    return visited[N - 1][M - 1]


M, N = map(int, input().split())  # 열, 행
graph = [list(map(int, input().rstrip())) for _ in range(N)]
print(bfs(0, 0))
print(dijkstra(0, 0))


"""
1261. 알고스팟 
    - 0-1 bfs 연습한다고 푼 문제
      시작 -> 끝 점으로 가는데 벽을 부순 최소의 개수를 출력한다.

    - 0-1 bfs는 가중치가 0 or 1인 경우에 사용할 수 있다.
    
    - 당연히 다익스트라로도 해결할 수 있었다.
"""