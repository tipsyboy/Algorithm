import sys
from collections import deque

input = sys.stdin.readline


def topological_sort(n, time, indegree, graph, target):
    q = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    rst = [0] * (n + 1)
    for i in range(1, n + 1):
        rst[i] = time[i - 1]

    while q:
        now = q.popleft()

        for adj in graph[now]:
            indegree[adj] -= 1  # 진입 차수 하나 제거
            rst[adj] = max(rst[adj], rst[now] + time[adj - 1])

            if indegree[adj] == 0:
                q.append(adj)

    return rst[target]


def solution():
    n, k = map(int, input().split())
    time = list(map(int, input().split()))  # time start idx 0

    indegree = [0] * (n + 1)  # 진입 차수
    graph = [[] for _ in range(n + 1)]
    for _ in range(k):
        x, y = map(int, input().split())
        graph[x].append(y)
        indegree[y] += 1

    target = int(input())  # target 건물 번호 w

    return topological_sort(n, time, indegree, graph, target)


tc = int(input())
for _ in range(tc):
    print(solution())
