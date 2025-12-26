# Dec 26, Fri 2025
# https://www.acmicpc.net/problem/1094

import sys

input = sys.stdin.readline

X = int(input())
ans = 0
for i in range(7):
    if X & (1 << i):
        ans += 1
print(ans)
