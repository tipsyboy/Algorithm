import sys
from collections import deque

input = sys.stdin.readline
MAXV = 10 ** 4


def eratos() -> list:
    sieve = [False, False] + [True] * MAXV

    for i in range(2, int(MAXV ** 0.5)):
        if not sieve[i]:
            continue

        for j in range(i + i, MAXV, i):
            if sieve[j]:
                sieve[j] = False

    return sieve


def bfs(start: int, target: int, sieve: list) -> int:
    visited = [0] * MAXV
    q = deque([start])

    while q:
        now = q.popleft()
        if now == target:
            return visited[now]

        str_now = str(now)
        for i in range(4):
            for j in range(10):
                nxt = int(str_now[:i] + str(j) + str_now[i + 1 :])
                if nxt < 1000:
                    continue
                if visited[nxt] != 0 or not sieve[nxt] or nxt == now:
                    continue

                q.append(nxt)
                visited[nxt] = visited[now] + 1

    return -1


TC = int(input())
sieve = eratos()
for _ in range(TC):
    start, target = map(int, input().split())

    ans = bfs(start, target, sieve)
    if ans == -1:
        print("Impossible")
    else:
        print(ans)
