# https://www.acmicpc.net/problem/1781

import sys
from heapq import heappush, heappop

input = sys.stdin.readline

N = int(input())
time_table = dict()
for _ in range(N):
    dead, noodle = map(int, input().split())

    if dead not in time_table:
        time_table[dead] = []

    time_table[dead].append(noodle)

pq = []
ans = 0
for t in range(N + 1, 0, -1):
    while t in time_table and time_table[t]:
        heappush(pq, -time_table[t].pop())

    if pq:
        ans += heappop(pq)

print(-ans)