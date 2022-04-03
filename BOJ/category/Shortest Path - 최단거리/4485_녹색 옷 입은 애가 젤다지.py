import sys
from heapq import heappush, heappop

input = sys.stdin.readline
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
INF = int(1e9)


def dijkstra(N, graph) -> int:
    pq = []
    heappush(pq, (graph[0][0], 0, 0))  # 가중치 / x, y
    dist = [[INF] * N for _ in range(N)]
    dist[0][0] = graph[0][0]

    while pq:
        now_cost, x, y = heappop(pq)

        if now_cost > dist[x][y]:
            continue

        for i in range(4):
            nx, ny = x + directions[i][0], y + directions[i][1]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            cost = now_cost + graph[nx][ny]
            if cost < dist[nx][ny]:
                dist[nx][ny] = cost
                heappush(pq, (cost, nx, ny))

    # print(*dist, sep="\n")
    return dist[N - 1][N - 1]


problem_number = 1
while True:
    N = int(input())
    if N == 0:
        break

    graph = [list(map(int, input().split())) for _ in range(N)]
    print("Problem %d: %d" % (problem_number, dijkstra(N, graph)))
    problem_number += 1

"""
    4485. 녹색 옷 입은 애가 젤다지?
    - 도둑 루피가 훔치는 돈의 양을 가중치로 생각하고, 2차원 배열을 다익스트라로 탐색
      상하좌우가 인접 노드가 되고 dist[][] 2차원 배열을 만들어서 다익스트라 가중치를 저장하면서 진행한다

    - 다익스트라를 1차원에서 2차원으로 확장한 것 빼고는 별 다를게 없었음.

"""
