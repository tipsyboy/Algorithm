import sys
from collections import deque

input = sys.stdin.readline


def topological_sorting() -> int:
    q = deque()
    for i in range(1, M + 1):
        if indegree[i] == 0:
            q.append(i)
            cnt_and_maxv[i][0], cnt_and_maxv[i][1] = 1, 1

    while q:
        now = q.popleft()

        if cnt_and_maxv[now][1] > 1:
            cnt_and_maxv[now][0] += 1
            cnt_and_maxv[now][1] = 1

        for adj in graph[now]:
            if cnt_and_maxv[now][0] > cnt_and_maxv[adj][0]:
                cnt_and_maxv[adj][0] = cnt_and_maxv[now][0]
                cnt_and_maxv[adj][1] = 1
            elif cnt_and_maxv[now][0] == cnt_and_maxv[adj][0]:
                cnt_and_maxv[adj][1] += 1

            indegree[adj] -= 1
            if indegree[adj] == 0:
                q.append(adj)

    return cnt_and_maxv[M][0]


TC = int(input())
for _ in range(TC):
    K, M, P = map(int, input().split())  # TC번호, 노드 수, 간선 수

    graph = [[] for _ in range(M + 1)]
    indegree = [0] * (M + 1)
    cnt_and_maxv = [[0, 0] for _ in range(M + 1)]

    for __ in range(P):
        u, v = map(int, input().split())
        graph[u].append(v)
        indegree[v] += 1

    print("%d %d" % (K, topological_sorting()))


"""
9470. Strahler 순서
    - 위상정렬 문제 
    
    - 포인트는 cnt_and_maxv를 관리하면서 값을 갱신하는데 있다. 
      처음에 1차원 배열로 잘 해볼랬는데, 중간에 값이 꼬이는 듯...?
"""