import sys
from heapq import heappush, heappop

input = sys.stdin.readline


n = int(input())
time = []
dist = []
for _ in range(n):
    com, v = input().split()
    if com == "T":
        heappush(time, int(v))
    else:
        heappush(dist, int(v))
