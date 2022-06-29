import sys
from collections import deque

input = sys.stdin.readline


def t_sorting() -> list:
    q = deque()
    need = [0] * (N + 1)
    need[N] = 1
    for i in range(1, N + 1):
        if ind_rvs[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()

        for adj in graph[now]:
            adj_node, cost = adj
            need[adj_node] += need[now] * cost

            ind_rvs[adj_node] -= 1
            if ind_rvs[adj_node] == 0:
                q.append(adj_node)

    return need


N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]
ind = [0] * (N + 1)
ind_rvs = [0] * (N + 1)
for _ in range(M):
    X, Y, K = map(int, input().split())
    graph[X].append((Y, K))
    ind_rvs[Y] += 1
    ind[X] += 1

need = t_sorting()
for i in range(1, N + 1):
    if ind[i]:
        continue
    print(i, need[i])