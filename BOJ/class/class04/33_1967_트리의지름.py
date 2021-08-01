import sys
from collections import deque
from heapq import heappush, heappop

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
INF = int(1e9)


# 1.
def solution_dfs():
    def dfs(node, now_cost):
        visited[node] = True

        for nxt, cost in graph[node]:
            if not visited[nxt]:
                dist.append((cost + now_cost, nxt))
                dfs(nxt, cost + now_cost)

    n = int(input())
    graph = [[] for _ in range(n + 1)]
    dist = []
    visited = [False] * (n + 1)

    for _ in range(n - 1):
        a, b, c = map(int, input().split())

        # undigraph
        graph[a].append((b, c))
        graph[b].append((a, c))

    if n == 1:
        return 0
    else:
        dfs(1, 0)
        node = max(dist)[1]
        dist = []
        visited = [False] * (n + 1)
        dfs(node, 0)

        return max(dist)[0]


# 2.
def bfs(start):
    q = deque([(start, 0)])  # start node, cost
    visited = [False] * (n + 1)
    visited[start] = True
    max_dist = 0
    idx = -1

    while q:
        now, cost = q.popleft()

        for nxt_node, nxt_cost in graph[now]:
            if not visited[nxt_node]:
                q.append((nxt_node, cost + nxt_cost))
                visited[nxt_node] = True
                if max_dist < cost + nxt_cost:
                    max_dist = cost + nxt_cost
                    idx = nxt_node

    return (idx, max_dist)


# 3.
def dijkstra(start):
    pq = []
    dist = [INF] * (n + 1)
    dist[start] = 0
    heappush(pq, (0, start))

    while pq:
        now_cost, now_node = heappop(pq)

        if dist[now_node] < now_cost:
            continue

        for nxt_node, nxt_cost in graph[now_node]:
            cost = now_cost + nxt_cost

            if cost < dist[nxt_node]:
                dist[nxt_node] = cost
                heappush(pq, (cost, nxt_node))

    return dist


# # 1. dfs
# print(solution_dfs())

# # 2. bfs
# n = int(input())
# graph = [[] for _ in range(n + 1)]

# for _ in range(n - 1):
#     a, b, c = map(int, input().split())

#     # undigraph
#     graph[a].append((b, c))
#     graph[b].append((a, c))

# # print rst value
# if n == 1:
#     print(0)
# else:
#     node = bfs(1)[0]
#     print(bfs(node)[1])

# 3.
n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b, c = map(int, input().split())

    # undigraph
    graph[a].append((b, c))
    graph[b].append((a, c))

if n == 0:
    print(0)
else:
    dist = dijkstra(1)
    print(max(dijkstra(dist.index(max(dist[1:])))[1:]))


"""
33. 1967 트리의 지름 (Gold 4)
    - 첫 번째 생각
      간선 비용이 -가 아닌 이상 leaf node 두개를 선택하는 것이 가장 큰 값을 가질 것이라고 생각하고 풀음.
      때문에, 루트 노드에서 각각의 leaf node까지의 간선비용을 구하고 leaf node 두개를 선택해서 비용을 더해준 다음
      각각의 부모노드가 같을때까지 탐색한 후에 부모노드까지의 비용을 두번 빼주는 식으로 계산 하려 했다. 

      하지만, 잠깐만 생각해봐도 leaf node 선택에 조합식 만큼의 시간이 필요하고(nC2), 부모노드를 찾아 나가는데 다시 로그시간만큼 걸리므로(맞나? 이진트리라고 생각하고 풀었다.)
      시간 초과가 날것이라고 생각함.

    - 이후에, 루트노드에서부터 가장 먼 노드를 선택하고 그 노드를 start node로 다시 가장 먼 node를 선택하는 방식으로 해결했다.
      트리를 쫙 펴는 행위를 한다고 생각했을때, root노드를 중심으로(원의 중심이 아님) 가장 먼 두 노드를 찾아내야 하는 것이므로 당연한 생각이었음..

    - 이후 풀이는 dfs, bfs, dijkstra 각각 풀이했다. 
      각각 방법만 살짝씩 다르고 구현은 전형적인 dfs, bfs, dijkstra다.
      알고리즘보다는 아이디어가 중요했던 문제라고 생각함.

    - n == 1 즉, 노드의 개수가 1개인 경우에는 0을 리턴하도록 예외처리 했다.
"""