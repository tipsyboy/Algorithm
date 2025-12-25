# https://www.acmicpc.net/problem/14235

import sys
from heapq import heappush, heappop

input = sys.stdin.readline

n = int(input())
pq = []
ans = []
for _ in range(n):
    x, *present = map(int, input().split())

    if x == 0:
        if pq:
            print(heappop(pq) * -1)
        else:
            print(-1)
    else:
        for i in range(x):
            heappush(pq, -present[i])
