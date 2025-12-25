# https://www.acmicpc.net/problem/5612

import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
ans = m
for _ in range(n):
    i, o = map(int, input().split())

    m += i - o
    if m < 0:
        ans = 0
        break

    ans = max(ans, m)

print(ans)
