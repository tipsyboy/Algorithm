# BOJ 1520 내리막 길

import sys
from heapq import heappush, heappop

input = sys.stdin.readline


def BFS(sy, sx) -> int:
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 북 남 서 동

    visited = [[0] * M for _ in range(N)]
    pq = []
    heappush(pq, (-graph[sy][sx], sy, sx))
    visited[sy][sx] = 1  # dp table

    while pq:
        height, y, x = heappop(pq)
        height *= -1

        for i in range(4):
            ny, nx = y + directions[i][0], x + directions[i][1]

            if ny < 0 or ny >= N or nx < 0 or nx >= M or graph[ny][nx] >= height:
                continue

            if not visited[ny][nx]:
                heappush(pq, (-graph[ny][nx], ny, nx))
            visited[ny][nx] += visited[y][x]

    # print(*visited, sep="\n")
    return visited[N - 1][M - 1]


N, M = map(int, input().split())  # 행, 열
graph = [list(map(int, input().split())) for _ in range(N)]

print(BFS(0, 0))


"""
    1520. 내리막 길 (그래프 탐색, DP?)
    - 내 기준 꽤나 까다로웠던 문제였음

    - 문제의 조건에 의해서 현재 위치 (row, col)에서 갈 수 있는 위치가 정해져 있다. (높은 값 -> 낮은 값)
    - 조건에 맞게 start -> end로 가는 모든 경로를 구하는 문제로 한 번 방문한 위치도 큐에 다시 들어가므로 모든 경로를 전부 탐색하면 TLE를 받게된다. 
      때문에 최대힙을 사용해서 높은 위치의 노드를 먼저 탐색하고 낮은 위치를 탐색한다. 
      '낮은 위치에 먼저 도달한 큐값이 높은 위치에서 올 수 있는 가능성을 열어두고 기다린다' 라고 생각하고 풀이했다.

    - 위의 풀이 방법을 사용하면 도달하는 위치에 오는 값을 전부 가져가야 하므로 dp가 사용된다. 
      때문에 visited[i][j]를 (i, j)에 도달할 수 있는 모든 경로라고 정의하고 pq를 사용해서 모든 위치에서 (i, j)로 올 수 있는 경로를 기다린 후에 출발한다. 

    - 파이썬에서 heapq는 최소힙으로 구현되어 있으므로 -1을 곱해서 최대힙을 표현했다.
"""