import sys
from heapq import heappush, heappop

input = sys.stdin.readline


def solution(arr):
    arr.sort(key=lambda x: x[1])
    pq = []

    for pay, day in arr:
        heappush(pq, pay)

        if len(pq) > day:
            heappop(pq)

    return sum(pq)


n = int(input())

arr = []
for _ in range(n):
    p, d = map(int, input().split())
    arr.append((p, d))

print(solution(arr))


"""
2109 순회강연 (Gold 3)
    - 오,, 생각보다 어려움..
"""