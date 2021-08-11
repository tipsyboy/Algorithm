import sys
from collections import deque

input = sys.stdin.readline


def bfs():
    visited = [False] * (n + 2)
    visited[0] = True
    q = deque([0])

    while q:
        now = q.popleft()

        for adj in graph[now]:
            if not visited[adj]:
                q.append(adj)
                visited[adj] = True

    if visited[n + 1]:
        return "happy"

    return "sad"


t = int(input())  # test case
for _ in range(t):
    n = int(input())  # 편의점 수

    pos = []
    for _ in range(n + 2):
        x, y = map(int, input().split())
        pos.append((x, y))

    graph = [[] for _ in range(n + 2)]
    for i in range(n + 1):
        for j in range(i + 1, n + 2):
            dist = abs(pos[i][0] - pos[j][0]) + abs(pos[i][1] - pos[j][1])

            if dist <= 1000:
                graph[i].append(j)
                graph[j].append(i)

    print(bfs())


"""
9205 맥주 마시면서 걸어가기 (Silver 1)
    - 간단한 bfs 문제라고 생각했는데, 좀 헷갈렸음..

    - 문제 풀이의 핵심은 이동 거리가 맥주 최대 범위인 1000을 넘지 않는 곳만 그래프가 이동할 수 있는 거리라고 생각하는 것
      즉, 간선이 주어지는 문제와 달리 직접 계산을 통해서 갈 수 있는 노드의 간선을 연결해서 문제를 풀면 된다. 

    - 간선을 직접 판단해서 만들어야 하는 점에서 난이도가 높다고 생각하는데, 골드도 안되서 의외였다.
      다양한 그래프 알고리즘으로 풀 수 있어서 그런가?

    - 플로이드-워셜 알고리즘 연습하려고 했는데, bfs로 더 많이 풀게 되는 것 같다..
"""