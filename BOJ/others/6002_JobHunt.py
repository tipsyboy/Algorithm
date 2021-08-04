import sys

input = sys.stdin.readline
negative_INF = -int(1e9)


def bellman_ford(start):
    dist = [negative_INF] * (n + 1)
    dist[start] = earn  ################씨ㅃㅃㅃㅃㅃㅃㅃㅃㅃㅃ

    for i in range(n):
        for edge in edges:
            now, nxt, cost = edge

            if dist[now] != negative_INF and dist[nxt] < dist[now] + cost:
                dist[nxt] = dist[now] + cost

                # 양수 간선 싸이클 존재
                if i == n - 1:
                    return -1

    return max(dist)


earn, m, n, f, s = map(int, input().split())  # 버는 돈 / 간선 수 / 노드 수 / 제트기 수 / start 지점
edges = []

for _ in range(m):
    a, b = map(int, input().split())

    edges.append((a, b, earn))

for _ in range(f):
    a, b, c = map(int, input().split())

    edges.append((a, b, earn - c))

print(bellman_ford(s))