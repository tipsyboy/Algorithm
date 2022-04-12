import sys
from collections import deque

input = sys.stdin.readline


def topology():
    q = deque()
    rst = [0] * (n + 1)

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append((i, 1))

    while q:
        now, semester = q.popleft()
        rst[now] = str(semester)

        for adj in graph[now]:
            indegree[adj] -= 1

            if indegree[adj] == 0:
                q.append((adj, semester + 1))

    return rst[1:]


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())

    graph[a].append(b)
    indegree[b] += 1

rst = topology()
print(" ".join(rst))