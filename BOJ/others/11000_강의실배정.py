import sys
from heapq import heappush, heappop

input = sys.stdin.readline


def solution(waiting):
    waiting.sort(key=lambda x: x[0])

    rst = 0
    end_time = []
    for w in waiting:
        start, end = w

        while end_time and end_time[0] <= start:
            heappop(end_time)

        heappush(end_time, end)

        rst = max(rst, len(end_time))

    return rst


n = int(input())

waiting = []
for _ in range(n):
    s, e = map(int, input().split())
    waiting.append((s, e))

print(solution(waiting))
