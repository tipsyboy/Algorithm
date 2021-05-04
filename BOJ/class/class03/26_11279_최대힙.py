import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    temp = int(input())

    if temp != 0:
        heapq.heappush(heap, (-temp, temp))
    else:
        if len(heap) > 0:
            print(heapq.heappop(heap)[1])
        else:
            print(0)


"""
    파이썬은 최소 힙만을 라이브러리로 제공한다. 
"""
