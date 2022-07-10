import sys
from heapq import heappush, heappop

input = sys.stdin.readline

N = int(input())
pq = []
for _ in range(N):
    x = int(input())

    if x == 0:
        ans = 0 if not pq else heappop(pq) * -1
        print(ans)
    else:
        heappush(pq, -x)

"""
11279. 최대 힙
    - 힙을 사용한 우선순위 큐 기본 문제
      파이썬은 최소 힙을 기본으로 사용하기 때문에 -1을 곱해서 최대 힙을 구현한다.
"""