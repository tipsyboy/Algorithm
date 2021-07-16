import sys
from heapq import heappush, heappop
input = sys.stdin.readline
INF = int(1e9)


def dijkstra(start, dest):
    pq = []
    dist[start] = 0
    heappush(pq, (0, start))  # 시작점 비용, 시작점

    while pq:
        now_cost, now_node = heappop(pq)  # 현재까지 cost, 거쳐가는 현재 노드

        # 방문 확인
        if dist[now_node] < now_cost:
            continue

        for adj in graph[now_node]:
            adj_node, adj_cost = adj

            # 현재 방문하고 있는 노드를 거쳐서 인접 노드까지 가는 경우에
            # 이미 인접노드까지 가는 비용이 더 적다면 이 루트를 선택할 이유가 없다.
            # 따라서 현재 방문 노드를 거쳐서 인접 노드까지 가는 경우만 탐색한다.
            if now_cost + adj_cost < dist[adj_node]:
                dist[adj_node] = now_cost + adj_cost
                heappush(pq, (now_cost + adj_cost, adj_node))

    # print(dist)

    return dist[dest]


n = int(input())  # 도시의 개수
e = int(input())  # 간선 개수
graph = [[] for _ in range(n)]  # 간선 정보

for _ in range(e):
    a, b, c = map(int, input().split())  # 출발지, 도착지, 비용

    graph[a - 1].append((b - 1, c))  # 0번 노드부터 시작하려고 -1 함

start, dest = map(int, input().split())  # 출발 노드, 목적지(도착지) 노드
dist = [INF] * n  # 거리

print(dijkstra(start - 1, dest - 1))  # 0번 노드부터 시작하려고 -1 함


"""
20. 1916 최소비용 구하기 (Gold 5)
    - 19. 1753과 구조적으로 완전히 같은 다익스트라(Dijkstra) 알고리즘 문제
    
    - 19. 1753 최단경로 문제를 풀고 바로 풀어서 별 문제 없이 바로 풀 수 있었다.
    
    - 구현 과정에서 변수가 조금 헷갈리는 문제가 있는데, 책에서 나온 것처럼 기계적으로도 코드가
      나올 수 있을 정도까지 연습해야 할 것 같다. 
"""
