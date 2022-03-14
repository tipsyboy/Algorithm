import sys
from collections import deque

input = sys.stdin.readline


def topological_sort(n, time, graph, indegree):
    rst = [0] * (n + 1)  # 결과 값
    for i in range(1, n + 1):
        rst[i] = time[i]

    q = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()

        for adj in graph[now]:
            indegree[adj] -= 1  # 진입차수 제거
            rst[adj] = max(rst[adj], rst[now] + time[adj])

            # 진입차수가 0이 된 새 노드 큐에 추가
            if indegree[adj] == 0:
                q.append(adj)

    return rst[1:]


def solution():
    n = int(input())
    time = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)  # 진입차수

    for i in range(1, n + 1):
        data = list(map(int, input().split()))

        time[i] = data[0]
        for j in data[1:-1]:
            graph[j].append(i)
            indegree[i] += 1

    rst = topological_sort(n, time, graph, indegree)

    for r in rst:
        print(r)


solution()


"""
1516. 게임 개발 (Gold 3)
    - 위상정렬
"""