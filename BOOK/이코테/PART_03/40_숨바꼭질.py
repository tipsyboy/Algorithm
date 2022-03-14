import sys
from heapq import heappush, heappop

input = sys.stdin.readline
INF = int(1e9)


def dijkstra(graph, start):
    pq = []
    dist = [INF] * (n + 1)
    heappush(pq, (0, start))
    dist[start] = 0

    while pq:
        now_cost, now_node = heappop(pq)

        if now_cost > dist[now_node]:
            continue

        for adj_node in graph[now_node]:
            cost = now_cost + 1
            if cost < dist[adj_node]:
                dist[adj_node] = cost
                heappush(pq, (cost, adj_node))

    return dist


n, m = map(int, input().split())
graph = [[] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())

    # undigraphs
    graph[a].append(b)
    graph[b].append(a)

dist = dijkstra(graph, 1)

max_node = 0
max_dist = 0
same_dist_node = []
for i in range(1, n + 1):
    if max_dist < dist[i]:
        max_dist = dist[i]
        max_node = i
        same_dist_node = [max_node]
    elif max_dist == dist[i]:
        same_dist_node.append(i)

print(max_node, max_dist, len(same_dist_node))


"""
40. 숨바꼭질 (p390)
    - 노드와 노드 사이의 거리가 모두 1인 최단거리 문제로 bfs를 사용해서 풀어도 되지만, 
      출력 조건에서 [숨을 헛간의 노드번호 / 최소 길의 개수 / 같은 거리의 헛간의 개수]를
      모두 출력해야 하므로, bfs를 사용하면 조금 귀찮을것 같아서 다익스트라로  해결했다. 

"""