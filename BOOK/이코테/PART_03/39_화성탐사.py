import sys
import time
from collections import deque
from heapq import heappush, heappop

input = sys.stdin.readline
INF = int(1e9)


def bfs(graph, sx, sy):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque([(sx, sy)])
    dist = [[INF] * n for _ in range(n)]
    dist[sx][sy] = graph[sx][sy]

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if dist[nx][ny] > dist[x][y] + graph[nx][ny]:
                    q.append((nx, ny))
                    dist[nx][ny] = dist[x][y] + graph[nx][ny]

    return dist[n - 1][n - 1]


def dijkstra(graph, sx, sy):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    pq = []
    dist = [[INF] * n for _ in range(n)]
    heappush(pq, (graph[sx][sy], sx, sy))
    dist[sx][sy] = graph[sx][sy]

    while pq:
        now_cost, x, y = heappop(pq)

        if now_cost > dist[x][y]:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                cost = now_cost + graph[nx][ny]
                if cost < dist[nx][ny]:
                    dist[nx][ny] = cost
                    heappush(pq, (cost, nx, ny))

    return dist[n - 1][n - 1]


t = int(input())  # test case

for _ in range(t):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]

    start = time.time()
    print(bfs(graph, 0, 0))
    print(time.time() - start)

    start = time.time()
    print(dijkstra(graph, 0, 0))  # 더 빠르군;;
    print(time.time() - start)


"""
39. 화성 탐사 
    - 탐색 그래프가 행렬의 형태로 4방향을 전부 검사하면서 진행한다. 

    - bfs, dijkstra 두 방법으로 해결했다.
"""


"""
13
9 0 5 1 1 5 3 5 4 2 2 3 7
4 1 2 1 6 5 3 5 4 2 2 3 7
0 7 6 1 6 8 5 5 4 2 2 3 7
1 1 7 8 3 2 3 5 4 2 2 3 7
9 4 0 7 6 4 1 5 4 2 2 3 7
5 8 3 2 4 8 3 5 4 2 2 3 7
7 4 8 4 8 3 4 5 4 2 2 3 7
7 4 8 4 8 3 4 5 4 2 2 3 7
7 4 8 4 8 3 4 5 4 2 2 3 7
7 4 8 4 8 3 4 5 4 2 2 3 7
7 4 8 4 8 3 4 5 4 2 2 3 7
7 4 8 4 8 3 4 5 4 2 2 3 7
7 4 8 4 8 3 4 5 4 2 2 3 7
"""