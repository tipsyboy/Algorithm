# https://www.acmicpc.net/problem/1182

import sys

input = sys.stdin.readline


def sol(depth: int, sumv: int) -> None:
    global ans

    if depth == N:
        if sumv == S:
            ans += 1
        return

    sol(depth + 1, sumv)
    sol(depth + 1, sumv + arr[depth])


N, S = map(int, input().split())
arr = list(map(int, input().split()))

ans = 0
sol(0, 0)
if S == 0:
    ans -= 1
print(ans)