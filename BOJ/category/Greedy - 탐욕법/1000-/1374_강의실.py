import sys
from heapq import heappush, heappop

input = sys.stdin.readline


def solution(wating):
    end_time = []
    rst = 0

    wating.sort(key=lambda x: x[0])

    for w in wating:
        start, end = w
        while end_time and end_time[0] <= start:
            heappop(end_time)

        heappush(end_time, end)
        rst = max(rst, len(end_time))

    return rst


n = int(input())
wating = []

for _ in range(n):
    a, s, e = map(int, input().split())
    wating.append((s, e))


print(solution(wating))
