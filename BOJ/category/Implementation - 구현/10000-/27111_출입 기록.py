# https://www.acmicpc.net/problem/27111

import sys

input = sys.stdin.readline

N = int(input())
barrack = set()
ans = 0
for _ in range(N):
    a, b = map(int, input().split())

    if b == 0:
        if a in barrack:
            barrack.remove(a)
        else:
            ans += 1
    elif b == 1:
        if a in barrack:
            ans += 1
        else:
            barrack.add(a)

ans += len(barrack)
print(ans)
