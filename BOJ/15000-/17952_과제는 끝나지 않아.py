# Nov 28, Fri 2025
# https://www.acmicpc.net/problem/17952

import sys

input = sys.stdin.readline

N = int(input())

stk = []
ans = 0
for _ in range(N):
    command, *options = map(int, input().split())

    if command == 1:
        stk.append((options[0], options[1]))

    if not stk:
        continue

    score, time = stk.pop()
    time -= 1
    if time == 0:
        ans += score
    else:
        stk.append((score, time))
print(ans)
