import sys
from collections import deque

input = sys.stdin.readline


def topological_sorting(n, graph, indegree, time):
    rst = [0] * (n + 1)
    for i in range(1, n + 1):
        rst[i] = time[i]

    q = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()

        for adj in graph[now]:
            rst[adj] = max(rst[adj], rst[now] + time[adj])
            indegree[adj] -= 1

            if indegree[adj] == 0:
                q.append(adj)

    return max(rst)


def solution():
    n = int(input())
    graph = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)  # 진입 차수
    time = [0] * (n + 1)  # 해당 작업의 걸리는 시간

    for i in range(1, n + 1):
        data = list(map(int, input().split()))

        time[i] = data[0]  # idx 0 - i번 작업이 걸리는 시간
        for j in data[2:]:
            indegree[i] += 1
            graph[j].append(i)

        # for j in range(data[1]):
        #     adj_node = data[j + 2]
        #     indegree[i] += 1
        #     graph[adj_node].append(i)

    return topological_sorting(n, graph, indegree, time)


print(solution())
