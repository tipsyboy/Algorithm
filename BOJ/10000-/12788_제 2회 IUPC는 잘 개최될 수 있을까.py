# https://www.acmicpc.net/problem/12788

import sys

input = sys.stdin.readline

N = int(input())
M, K = map(int, input().split())
pens = sorted(map(int, input().split()), reverse=True)

s = M * K
now, ans = 0, 0
for pen in pens:
    if now >= s:
        break

    now += pen
    ans += 1

print(ans if now >= s else "STRESS")
