import sys
from collections import deque

input = sys.stdin.readline
INF = int(1e9)


def bfs(start):
    q = deque([start])
    dist = [INF] * (v + 1)
    dist[start] = 0

    while q:
        now = q.popleft()

        for adj in graph[now]:
            adj_node, adj_cost = adj

            if dist[adj_node] == INF:
                q.append(adj_node)
                dist[adj_node] = dist[now] + adj_cost

    return dist


v = int(input())
graph = [[] * (v + 1) for _ in range(v + 1)]

for _ in range(v):
    temp = list(map(int, input().split()))

    for i in range(1, len(temp) // 2):
        graph[temp[0]].append((temp[i * 2 - 1], temp[2 * i]))

dist_start = bfs(1)
idx = dist_start.index(max(dist_start[1:]))
dist_last = bfs(idx)

print(max(dist_last[1:]))


"""
42. 1167 트리의 지름 (Gold 3)
    - 이전의 풀었던 1167_트리의 지름이랑 거의 같은 문제이다. 
      
      루트 노드에서 가장 먼 노드를 찾고, 해당 노드를 기준으로 다시 가장 먼 노드를 찾으면 지름을 구할 수 있다. 
      대신 트리의 루트가 정해져 있지 않은데, graph의 아무 점이나 루트로 보고 수행하면 같은 결과를 얻을 수 있다. 
    
    - 처음에는 dfs로 풀었고 코드는 날려버렸다..
      다른 탐색 알고리즘을 통해서 풀어도 같은 결과를 얻을 수 있을것 같다.
"""