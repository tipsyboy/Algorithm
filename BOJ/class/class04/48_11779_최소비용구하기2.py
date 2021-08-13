import sys
from heapq import heappush, heappop

input = sys.stdin.readline
INF = int(1e9)


def dijkstra(start, dest):
    pq = []
    dist = [INF] * (n + 1)
    route = [[] * (n + 1) for _ in range(n + 1)]

    # 초기화
    heappush(pq, (0, start))
    dist[start] = 0
    route[start].append(start)

    while pq:
        now_cost, now_node = heappop(pq)

        if now_cost > dist[now_node]:
            continue

        for adj in graph[now_node]:
            adj_node, adj_cost = adj
            cost = now_cost + adj_cost

            if cost < dist[adj_node]:
                dist[adj_node] = cost
                heappush(pq, (cost, adj_node))
                route[adj_node] = []

                for node in route[now_node]:
                    route[adj_node].append(node)
                route[adj_node].append(adj_node)

    # 출력
    print(dist[dest])
    print(len(route[dest]))
    for i in range(len(route[dest])):
        print(route[dest][i], end=" ")
    print()


def dijkstra2(start, dest):
    pq = []
    dist = [INF] * (n + 1)
    route = [-1] * (n + 1)  # 경로를 추적하는 리스트

    # 초기화
    heappush(pq, (0, start))
    dist[start] = 0

    while pq:
        now_cost, now_node = heappop(pq)

        if now_cost > dist[now_node]:
            continue

        for adj in graph[now_node]:
            adj_node, adj_cost = adj

            cost = adj_cost + now_cost

            # 값 갱신
            if cost < dist[adj_node]:
                dist[adj_node] = cost
                heappush(pq, (cost, adj_node))
                route[adj_node] = now_node

    count = 0

    rst_route = []
    temp = dest
    rst_route.append(dest)
    while route[temp] != -1:
        rst_route.append(route[temp])
        temp = route[temp]
    rst_route.reverse()

    print(dist[dest])
    print(len(rst_route))
    for i in rst_route:
        print(i, end=" ")
    print()


n = int(input())
m = int(input())
graph = [[] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())

    graph[a].append((b, c))

start, dest = map(int, input().split())

# #
# dijkstra(start, dest)

#
dijkstra2(start, dest)


"""
48. 11779 최소비용 구하기2 (Gold 3)
    - 일반적인 dijkstra 알고리즘 문제에다가 최단거리의 경로까지 추가된 문제
    
    1. 최단거리
    - 그냥 다익스트라

    2. 경로 찾기
    - 1) route 리스트를 따로 둔 후에 첫 시작점의 값을 1을 주고 최단거리의 값이 갱신될 때마다 
         이전 노드의 route 리스트의 값을 그대로 가져온 후에 인접 노드를 추가해서 리스트를 만들어 줬다. 

    - 2) 구글링 이후에 찾아보니까 route를 1차원으로 선언하고 시작점을 -1 준 이후에 
         값이 갱신될 때마다 이전 노드의 번호만 리스트에 넣어줘서 마지막에 while문을 돌면서 경로를 되추적하는 방식을 사용했다. 
         생각 1도 못했는데 좋은 방법인거 같아서 dijkstra2()로 다시 구현해봤다.

    3. 경로의 개수
    - 그냥 route의 dest의 길이를 출력하면 된다. 
"""