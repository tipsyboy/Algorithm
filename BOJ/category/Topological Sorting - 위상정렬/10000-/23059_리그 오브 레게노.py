# https://www.acmicpc.net/problem/23059

import sys
from collections import deque

input = sys.stdin.readline


def topological_sorting() -> list:
    q = deque()

    #
    for item in indegree.keys():
        if indegree[item] == 0:
            q.append(item)
    q = deque(sorted(q))

    rst = []
    while q:
        for _ in range(len(q)):
            now_item = q.popleft()
            rst.append(now_item)

            if now_item not in graph:
                continue

            for nxt in graph[now_item]:
                indegree[nxt] -= 1

                if indegree[nxt] == 0:
                    q.append(nxt)

        q = deque(sorted(q))

    if len(indegree) != len(rst):
        return []

    return rst


N = int(input())
graph = dict()
indegree = dict()
for _ in range(N):
    A, B = input().split()
    indegree[A] = indegree.get(A, 0)
    indegree[B] = indegree.get(B, 0) + 1

    if A not in graph:
        graph[A] = list()
    graph[A].append(B)


rst = topological_sorting()
if not rst:
    print(-1)
else:
    print("\n".join(rst))