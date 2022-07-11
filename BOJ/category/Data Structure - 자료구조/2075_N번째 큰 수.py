import sys
from heapq import heappush, heappop, heapify

input = sys.stdin.readline

N = int(input())

pq = list(map(int, input().split()))
heapify(pq)
for _ in range(N - 1):
    temp = list(map(int, input().split()))

    for i in range(N):
        if temp[i] > pq[0]:
            heappop(pq)
            heappush(pq, temp[i])

print(heappop(pq))


"""
2075. N번째 큰 수 
    - 우선순위 큐, 
      잠깐 헤맸음 메모리 12MB 처리가 생각 막은듯.
"""