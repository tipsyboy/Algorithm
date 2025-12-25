# https://www.acmicpc.net/problem/18429

import sys

input = sys.stdin.readline


def bt(day: int, w: int) -> None:
    global ans

    if w < 500:
        return

    if day == N:
        ans += 1
        return

    for i in range(N):
        if used[i]:
            continue
        used[i] = True
        bt(day + 1, w + kits[i] - K)
        used[i] = False


N, K = map(int, input().split())
kits = list(map(int, input().split()))
used = [False] * N

ans = 0
bt(0, 500)
print(ans)
