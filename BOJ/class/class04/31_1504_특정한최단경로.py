import sys
from heapq import heappush, heappop
input = sys.stdin.readline
INF = int(1e9)


# 2. Dijkstra 알고리즘
def dijkstra(start):
    pq = []  # heapq
    heappush(pq, (0, start))  # 현재까지 dist, node
    dist = [INF] * (n + 1)
    dist[start] = 0

    while pq:
        now_dist, now_node = heappop(pq)

        # 간선 비용이 -는 아닐테니까 현재 dist 값이 더 작으면 계산할 필요가 없음
        if dist[now_node] < now_dist:
            continue

        # check adjacent node
        for adj in graph[now_node]:
            adj_node, adj_dist = adj
            cost = now_dist + adj_dist

            # update dist table
            if cost < dist[adj_node]:
                dist[adj_node] = cost
                heappush(pq, (cost, adj_node))

    return dist


# 1. input & init
n, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(e):
    a, b, c = map(int, input().split())

    # undirected graph
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())  # 반드시 거쳐야하는 두 정점

# 3. 최단 경로 찾아내기
dist_start = dijkstra(1)
dist_v1 = dijkstra(v1)
dist_v2 = dijkstra(v2)

# start -> v1 -> v2 -> destination(정점 n)
rst1 = dist_start[v1] + dist_v1[v2] + dist_v2[n]
# start -> v2 -> v1 -> destination(정점 n)
rst2 = dist_start[v2] + dist_v2[v1] + dist_v1[n]

# 4. 결과 값
rst = min(rst1, rst2)
print(rst) if rst < INF else print(-1)


"""
31. 1504 특정한 최단 경로
    - 다익스트라 알고리즘을 여러번 사용한다.
      한 정점에서 모든 정점으로 가는 최단 거리를 찾아냄. (예전 수학문제 네모칸 최단거리 찾기 처럼)

      문제의 조건 때문에 헷갈렸으나, 상관 없었다. 

    - 91%에서 계속 WA받아서 게시판 찾아봤는데, 반례도 다 통과해서 빨리 못찾았으면 멘탈 나갈뻔 했다.
      
      rst를 구하는 과정에서 2INF, 3INF가 나올수 있으므로 rst != INF 조건을 주는 것이 아니라 rst < INF 조건을 줘야한다. 
    
    - 그냥 평범한 다익스트라 알고리즘 문제
"""
