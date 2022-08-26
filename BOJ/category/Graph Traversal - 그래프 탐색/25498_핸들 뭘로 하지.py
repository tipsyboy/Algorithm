# https://www.acmicpc.net/problem/25498

import sys
from collections import deque

input = sys.stdin.readline


def bfs(start: int) -> str:
    ans = tree_char[1]
    q = deque([start])
    visited = [False] * (N + 1)
    visited[start] = True
    while q:
        alpha = None
        candidate = []
        for _ in range(len(q)):
            now = q.popleft()

            for ch in tree[now]:
                if visited[ch]:
                    continue

                if alpha == None:
                    alpha = tree_char[ch]
                    candidate.append(ch)
                elif alpha == tree_char[ch]:
                    candidate.append(ch)
                elif alpha < tree_char[ch]:
                    alpha = tree_char[ch]
                    candidate = [ch]

                visited[ch] = True

        if alpha != None:
            ans += alpha
        q = deque(candidate)

    return ans


N = int(input())
tree_char = "0" + input().rstrip()
tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

print(bfs(1))


"""
25498. 핸들 뭘로 하지
    - 2022 ICPC Sinchon Summer Algorithm Camp Open Contest에서 만난 문제
      bfs는 상상도 못했다. 아이디어면 어려웠음..

    - 트리를 레벨마다 너비 우선 탐색으로 탐색하면서 사전 순으로 가장 나중에 나오는 알파벳이 해당 레벨의 단어가 된다. 
      이를 생각하면서 bfs를 돌려주면 최적해를 찾을 수 있다. 
"""