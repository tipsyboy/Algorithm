# https://www.acmicpc.net/problem/14248

import sys
from collections import deque

input = sys.stdin.readline


def stone_bridge(start: int) -> int:
    q = deque([start])
    visited = [False] * n
    visited[start] = True

    cnt = 1
    while q:
        now = q.popleft()

        for i in [-1, 1]:
            nxt = now + bridge[now] * i

            if nxt < 0 or nxt >= n:
                continue
            if visited[nxt]:
                continue

            q.append(nxt)
            visited[nxt] = True
            cnt += 1

    return cnt


n = int(input())
bridge = list(map(int, input().split()))
s = int(input())
print(stone_bridge(s - 1))


"""
14248. 점프 점프
    - 1차원 그래프 탐색
"""