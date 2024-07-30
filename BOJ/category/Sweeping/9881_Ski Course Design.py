# 2024.06.03 MON
# https://www.acmicpc.net/problem/9881

import sys

input = sys.stdin.readline
MAX_HEIGHT = 100

N = int(input())
hills = []
for _ in range(N):
    hills.append(int(input()))
hills.sort()

ans = float("inf")
for s in range(MAX_HEIGHT - 17 + 1):
    e = s + 17

    pay = 0
    for hill in hills:
        if hill < s:
            pay += (s - hill) ** 2
        elif hill > e:
            pay += (hill - e) ** 2

    ans = min(ans, pay)
print(ans)
