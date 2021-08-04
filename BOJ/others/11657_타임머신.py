import sys

input = sys.stdin.readline
INF = int(1e9)


def bellman_ford(start):
    dist = [INF] * (n + 1)
    dist[start] = 0

    for i in range(n):
        for edge in edges:
            now, nxt_node, cost = edge

            if dist[now] != INF and dist[nxt_node] > dist[now] + cost:
                dist[nxt_node] = dist[now] + cost

                if i == n - 1:
                    return []  # 빈 리스트

    return dist


n, m = map(int, input().split())
edges = []  # 전체 간선

for _ in range(m):
    a, b, c = map(int, input().split())

    edges.append((a, b, c))

dist = bellman_ford(1)

if not dist:
    print(-1)
else:
    for i in range(2, n + 1):
        print(-1) if dist[i] == INF else print(dist[i])