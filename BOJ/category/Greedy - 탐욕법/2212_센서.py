import sys
from heapq import heappush, heappop

input = sys.stdin.readline

N = int(input())
K = int(input())
arr = list(map(int, input().split()))

ans = 0
if N > K:
    arr.sort()
    pq = []
    for i in range(1, N):
        heappush(pq, -(arr[i] - arr[i - 1]))
    for _ in range(K - 1):
        heappop(pq)
    for _ in range(len(pq)):
        ans += heappop(pq) * -1
print(ans)

"""
2212. 센서
    - 이거 문제 이해하면 별거 아닌데, 지문 이해가 안됐었음.

    - 요점은 N개의 센서를 K뭉치로 만들어서 그 뭉치 안에 있는 센서끼리의 거리를 최소화 하는 것
      즉, 가장 거리가 긴 두 센서부터 끊어서 두 뭉치로 만든다. (K-1)번 만큼 끊어서 K뭉치 만들기
"""