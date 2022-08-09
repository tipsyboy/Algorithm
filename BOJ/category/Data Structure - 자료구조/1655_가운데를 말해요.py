import sys
from heapq import heappush, heappop

input = sys.stdin.readline

N = int(input())

A = []  # max heap
B = []  # min heap
ans = []
for i in range(N):
    x = int(input())

    if i % 2 == 0:
        heappush(A, -x)
    else:
        heappush(B, x)

    if B and (A[0] * -1 > B[0]):
        heappush(B, heappop(A) * -1)
        heappush(A, heappop(B) * -1)

    ans.append(A[0] * -1)

print("\n".join(map(str, ans)))


"""
1655. 가운데를 말해요
    - 주어진 수까지의 집합에서 계속해서 중간의 수를 출력한다. 짝수 개의 경우 더 작은 수를 출력한다. 

    - 우선순위 큐를 사용해서 풀이

    - 수의 집합을 A, B로 나누어서 사용한다. 
      두 집합 A, B가 있을때, A의 모든 원소가 B의 모든 원소보다 작거나 같고 
      n(X)를 X집합의 개수라고 했을때, n(A) = n(B) or n(A) = n(B) + 1 인 경우 
      A의 최댓값이 전체 집합 A+B의 중간값이 되고 이것이 문제의 최적해가 된다. 
"""