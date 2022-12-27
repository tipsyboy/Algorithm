# https://www.acmicpc.net/problem/2251

import sys
from collections import deque

input = sys.stdin.readline
action = [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]  # A: 0, B: 1, C: 2


def bfs(BOTTLES_MAX: list) -> list:
    q = deque([[0, 0, BOTTLES_MAX[2]]])
    visited = set()
    visited.add((0, 0, BOTTLES_MAX[2]))
    ans = set([BOTTLES_MAX[2]])

    while q:
        bottles = q.popleft()
        for i in range(6):
            f = action[i][0]  # from
            t = action[i][1]  # to
            water = min(bottles[f], BOTTLES_MAX[t] - bottles[t])
            nxt = [bottles[0], bottles[1], bottles[2]]

            nxt[f] -= water
            nxt[t] += water
            nxt = tuple(nxt)
            if nxt in visited:
                continue

            q.append(list(nxt))
            visited.add(nxt)
            if nxt[0] == 0:
                ans.add(nxt[2])

    return sorted(list(ans))


BOTTLES_MAX = list(map(int, input().split()))
print(*bfs(BOTTLES_MAX))