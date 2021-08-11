import sys
from heapq import heappush, heappop

input = sys.stdin.readline
INF = int(1e9)


# 1)
def floyd_washall():
    graph = [[INF] * (n + 1) for _ in range(n + 1)]
    get_item_max = 0  # 얻을 수 있는 item의 개수

    # 자기 자신으로 가는 루트 초기화
    for i in range(1, n + 1):
        graph[i][i] = 0

    # graph 입력
    for _ in range(r):
        a, b, c = map(int, input().split())  # a <-> b, cost c
        # undigraph
        graph[a][b] = c
        graph[b][a] = c

    #
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    #
    for i in range(1, n + 1):
        temp = 0
        for j in range(1, n + 1):
            if graph[i][j] <= m:
                temp += item[j - 1]
        get_item_max = max(get_item_max, temp)

    return get_item_max


# 2) Dijkstra
def solution_dijkstra():
    graph = [[] * (n + 1) for _ in range(n + 1)]
    get_item_max = 0

    #
    for _ in range(r):
        a, b, c = map(int, input().split())

        # undigraph
        graph[a].append((b, c))
        graph[b].append((a, c))

    def dijkstra(start):
        pq = []
        dist = [INF] * (n + 1)
        dist[start] = 0
        heappush(pq, (0, start))

        while pq:
            now_cost, now_node = heappop(pq)

            if now_cost > dist[now_node]:
                continue

            for adj in graph[now_node]:
                adj_node, adj_cost = adj

                cost = now_cost + adj_cost

                if dist[adj_node] > cost:
                    dist[adj_node] = cost
                    heappush(pq, (cost, adj_node))

        return dist[1:]

    for i in range(1, n + 1):
        dist = dijkstra(i)
        temp = 0

        for j in range(n):
            if dist[j] <= m:
                temp += item[j]

        get_item_max = max(get_item_max, temp)

    return get_item_max


n, m, r = map(int, input().split())  # node, 수색범위, edge 수
item = list(map(int, input().split()))  # 각 node에서 얻을 수 있는 아이템의 개수

# # 1) Floyd-Washall 풀이
# print(floyd_washall())

# 2) Dijkstra 풀이
print(solution_dijkstra())


"""
41. 14938 서강그라운드 (Gold 4)
    - 특별한 점이 없는 최단거리 알고리즘 문제, 
      마지막에 item을 얻을 수 있는 부분만 추가되서 어디서 출발하는게 가장 큰 이득을 갖는지만 더 생각해주면 된다.  
    
    - 간선 값이 양수인 최단거리 알고리즘인 Dijkstra와 Floyd-Washall 두 가지를 사용해서 풀이했다.
      Dijkstra 쪽이 시간상 이득이 더 컸다.
"""