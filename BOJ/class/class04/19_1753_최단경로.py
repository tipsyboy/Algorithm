import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)


# 우선순위 큐를 이용한 다익스트라 구현 (ElogV)
def dijkstra(start):
    pq = []  # heap
    dist[start] = 0  # start node는 dist 0
    heapq.heappush(pq, (0, start))  # cost val, node

    while pq:
        now_dist, now_node = heapq.heappop(pq)  # 현재 노드까지 온 비용, 거쳐가는 노드

        # 방문 확인 -
        if dist[now_node] < now_dist:
            continue

        for adj in graph[now_node]:
            adj_node, adj_cost = adj  # now_node의 인접노드, 거기까지 가는 비용

            if now_dist + adj_cost < dist[adj_node]:
                dist[adj_node] = now_dist + adj_cost
                heapq.heappush(pq, (now_dist + adj_cost, adj_node))


n, e = map(int, input().split())  # node, edge
start = int(input()) - 1  # graph index 때문
graph = [[] for _ in range(n)]
dist = [INF] * n  # distance

# 간선 입력
for _ in range(e):
    a, b, c = map(int, input().split())  # from, to, cost

    graph[a - 1].append((b - 1, c))

dijkstra(start)


# print(dist)
# for i in dist:
#     print("INF") if i == INF else print(i)


"""
19. 1753 최단경로 (Gold 5)
    - 다익스트라 알고리즘 가장 기초적인 문제로 문제 이름도 최단경로이다. 필수문제!

    1. 첫 번째 시도
    - DFS로 해결할 수 있지 않을까 해서 시도 했는데, MLE로 실패했다. (test case는 통과)
      이유는 잘...

    2. 다익스트라 알고리즘 
    - 다익스트라 알고리즘으로 해결했지만, 직관적인 방법을 사용했고, 매 노드마다(n) 최단 거리를 찾느라 
      dist[]를 순회했다. (n) => O(n^2)
      당연히 TLE로 실패했다. 

    3. 개선된 다익스트라 알고리즘 
    - 우선순위 큐를 이용해서 매 노드마다 최단 거리를 찾는 과정을 파이썬 heapq를 통해서 구현했다. 
      heapq의 삽입/삭제 연산은 각각 O(logn)이므로 2logn이고,
      매 노드마다 모든 간선을 탐색하므로 n의 시간 복잡도를 갖는다. 
      따라서 2ElogV의 복잡도를 갖고 빅-오 표현법으로 ElogV이므로 O(nlogn)의 시간복잡도를 갖는다. 
      AC 받았다. 
"""
