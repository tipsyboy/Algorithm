import sys
from heapq import heappush, heappop

input = sys.stdin.readline


n = int(input())

pq = []
for _ in range(n):
    heappush(pq, int(input()))

rst = 0
while len(pq) > 1:
    a = heappop(pq)
    b = heappop(pq)
    temp = a + b
    rst += temp
    heappush(pq, temp)

print(rst)


# 단순 오름차순이 아님 - 반례: [20, 40, 50, 55, 70]
