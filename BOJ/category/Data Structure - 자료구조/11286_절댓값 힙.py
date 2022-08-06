import sys
from heapq import heappush, heappop

input = sys.stdin.readline


def solution():
    n = int(input())
    pq = []

    for _ in range(n):
        x = int(input())

        if x == 0:
            if pq:
                print(heappop(pq)[1])
            else:
                print(0)
        else:
            heappush(pq, (abs(x), x))


solution()
