# https://www.acmicpc.net/problem/1417

import sys
from heapq import heappush, heappop

input = sys.stdin.readline

N = int(input())
dasom = int(input())
others = []
for _ in range(N - 1):
    heappush(others, int(input()) * -1)

temp = dasom
if N > 1:
    while dasom <= others[0] * -1:
        o = heappop(others) * -1

        dasom += 1
        heappush(others, (o - 1) * -1)
print(dasom - temp)


"""
1417. 국회의원 선거
    - 간단하게 가장 많은거 계속 뽑아서 구현
"""