import sys
from collections import deque

input = sys.stdin.readline


def topology(n, graph, indegree):
    q = deque()

    #
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    #
    certain = True  # 명확한지
    cycle = False  # cycle이 존재하는지
    rst = []
    for _ in range(n):
        if not q:  # 아직 n번 수행하지 않았는데, 큐가 비어있는 경우
            cycle = True
            break

        if len(q) >= 2:
            certain = False
            break

        now = q.popleft()
        rst.append(str(now))
        for adj in graph[now]:
            indegree[adj] -= 1

            if indegree[adj] == 0:
                q.append(adj)

    #
    if cycle:
        return "IMPOSSIBLE"
    elif not certain:
        return "?"
    else:
        return " ".join(rst)


def solution():
    n = int(input())
    ranking = list(map(int, input().split()))

    # input graph, indegree
    indegree = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    for i in range(n - 1):
        for j in range(i + 1, n):
            graph[ranking[i]].append(ranking[j])
            indegree[ranking[j]] += 1

    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())

        if a in set(graph[b]):
            graph[a].append(b)
            graph[b].remove(a)
            indegree[a] -= 1
            indegree[b] += 1
        else:
            graph[b].append(a)
            graph[a].remove(b)
            indegree[a] += 1
            indegree[b] -= 1

    print(topology(n, graph, indegree))


tc = int(input())  # test case

for _ in range(tc):
    solution()