import sys
from heapq import heappush, heappop

input = sys.stdin.readline
INF = int(1e9)


# 1) 일반적인 Dijkstra
def solution1():
    def dijkstra1(start):
        pq = []
        dist = [INF] * (n + 1)
        heappush(pq, (0, start))
        dist[start] = 0

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

        return dist

    graph = [[] * (n + 1) for _ in range(n + 1)]
    max_value = 0

    for _ in range(m):
        a, b, c = map(int, input().split())

        graph[a].append((b, c))

    # 파티 위치에서 자신의 마을로 돌아가는 길
    dist_x = dijkstra(x)
    # 각각의 마을에서 파티로 가는길
    for i in range(1, n + 1):
        if i == x:
            continue
        dist = dijkstra(i)
        max_value = max(max_value, dist[x] + dist_x[i])

    return max_value


# 2) 문제의 특성 이용 Dijkstra2
def solution2():
    def dijkstra(start):
        pq = []
        dist = [INF] * (n + 1)
        heappush(pq, (0, start))
        dist[start] = 0

        while pq:
            now_cost, now_node = heappop(pq)

            # Dijkstra의 greedy한 성질을 이용해서 x 노드에 도달하면 리턴한다.
            # 파티 장소에서 각자의 집으로 돌아가는 길은 전체를 구해야 하므로 걸러낸다.
            if now_node == x and start != x:
                return dist

            if now_cost > dist[now_node]:
                continue

            for adj in graph[now_node]:
                adj_node, adj_cost = adj
                cost = now_cost + adj_cost

                if cost < dist[adj_node]:
                    dist[adj_node] = cost
                    heappush(pq, (cost, adj_node))

        return dist

    graph = [[] * (n + 1) for _ in range(n + 1)]
    max_value = 0

    for _ in range(m):
        a, b, c = map(int, input().split())

        graph[a].append((b, c))

    # 파티 위치에서 자신의 마을로 돌아가는 길
    dist_x = dijkstra(x)

    # 각각의 마을에서 파티로 가는길
    for i in range(1, n + 1):
        if i == x:
            continue

        dist = dijkstra(i)
        max_value = max(max_value, dist[x] + dist_x[i])

    return max_value


# 3) 문제의 특성을 이용한 Dijkstra3
def solution3():
    def dijkstra(start, graph):
        pq = []
        dist = [INF] * (n + 1)
        heappush(pq, (0, start))
        dist[start] = 0

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

        return dist

    graph = [[] * (n + 1) for _ in range(n + 1)]
    graph_r = [[] * (n + 1) for _ in range(n + 1)]
    max_value = 0

    for _ in range(m):
        a, b, c = map(int, input().split())

        graph[a].append((b, c))
        graph_r[b].append((a, c))

    dist = dijkstra(x, graph)
    dist_r = dijkstra(x, graph_r)

    # sum_dist = [x + y for x, y in zip(dist, dist_r)]
    for i in range(1, n + 1):
        dist[i] = dist[i] + dist_r[i]

    return max(dist[1:])


n, m, x = map(int, input().split())  # node, edge, destination

# print(solution1())
# print(solution2())
print(solution3())


"""
43. 1238 파티 (Gold 3)
    - 그냥 그래프 최단거리를 찾는 문제여서 특별한 점은 없었으나, 파티의 위치가 x로 고정되어 있는 상황이라서
      시간복잡도를 크게 줄일 수 있는 방법들이 있었다. 

    1.
    - 첫 번째는 그냥 Dijkstra를 이용한 방법이다. 
      파티 지점에서 각각의 마을로 돌아가는 dist를 먼저 구해주고
      각각의 다익스트라를 돌려서 x점으로 가는 수와 함께 더해서 max 값을 찾는다. 

    2.
    - 다익스트라가 그리디 알고리즘의 일종인 것을 이용해서, x의 dist를 구하면 그냥 리턴하는 방식이다. 
      다익스트라 특징상 이미 선택된 node의 값은 갱신되지 않으므로 이렇게 해도 문제가 없고,
      대신에 x지점에서 각각의 모든 마을로 돌아가는 길은 구해주어야 하므로 start != x인 경우는 제외해줬다. 
      1260ms -> 460ms로 약 800ms 가량 줄였다. 

    3.
    - 이번에도 파티 지점이 x점으로 고정되어 있는 것을 이용한다. 
      모든 인원은 각자의 지점 i에서 x로 다시 x에서 i로 이동한다. 즉, i -> x -> i인데
      앞의 i -> x인 경우는 역방향 그래프인 경우에 x -> i와 같은 결과를 갖는다. 
      따라서, graph 입력시에 역방향 그래프를 하나 더 받아서 i -> x 때는 역방향 그래프로 다익스트라
      x -> i는 정방향 그래프로 다익스트라. 총 2번의 다익스트라 알고리즘으로 값을 구할 수 있다. 

    - zip()

    4. 
    - 문제를 보면 당연히 플로이드-워셜로도 풀 수 있겠지만 귀찮아서 여기 적지는 않는다.
"""