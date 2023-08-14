# https://www.acmicpc.net/problem/1039

"""
1039. 교환
    - 매번 회차에서 모든 경우의 수를 따지고 다음 회차로 넘김
    - 회차에서 겹치는 수가 있는 경우를 set()으로 제거
"""

import sys
from collections import deque

input = sys.stdin.readline


def bfs(start: str, K: int) -> str:
    q = deque([(start, 0)])
    visited = set([(start, 0)])
    length = len(start)

    ans = []
    while q:
        cur, cnt = q.popleft()
        if cnt == K:
            ans.append(cur)
            continue

        temp = list(cur)
        for i in range(length - 1):
            for j in range(i + 1, length):
                if i == 0 and temp[j] == "0":
                    continue

                temp[i], temp[j] = temp[j], temp[i]
                nxt = "".join(temp)
                if (nxt, cnt + 1) not in visited:
                    visited.add((nxt, cnt + 1))
                    q.append((nxt, cnt + 1))
                temp[i], temp[j] = temp[j], temp[i]

    return -1 if not ans else int(sorted(ans, reverse=True)[0])


N, K = input().split()
print(bfs(N, int(K)))