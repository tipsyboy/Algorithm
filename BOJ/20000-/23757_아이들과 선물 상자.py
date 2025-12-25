# 2024.12.11 WED
# https://www.acmicpc.net/problem/23757

import sys
from heapq import heappush, heappop, heapify

input = sys.stdin.readline

N, M = map(int, input().split())
c = list(map(lambda x: -int(x), input().split()))
w = list(map(int, input().split()))

heapify(c)

ans = 1
for i in range(M):
    v = -1 * heappop(c)
    if v < w[i]:
        ans = 0
        break

    v -= w[i]
    if v > 0:
        heappush(c, -v)

print(ans)
