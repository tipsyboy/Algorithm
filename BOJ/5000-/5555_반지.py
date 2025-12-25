# https://www.acmicpc.net/problem/5555

import sys

input = sys.stdin.readline

search = input().rstrip()
N = int(input())

ans = 0
for _ in range(N):
    ring = input().rstrip()
    ring = ring + ring[:-1]

    if search in ring:
        ans += 1

print(ans)
