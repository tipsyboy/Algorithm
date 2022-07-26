import sys
from heapq import heappush, heappop, heapify

input = sys.stdin.readline

TC = int(input())
for _ in range(TC):
    K = int(input())
    pq = list(map(int, input().split()))
    heapify(pq)

    ans = 0
    while len(pq) > 1:
        a, b = heappop(pq), heappop(pq)
        ans += a + b
        heappush(pq, a + b)

    print(ans)


"""
13975. 파일 합치기 3
    - 파일을 합치는데 다른 조건이 없고 모든 장을 합치는데 최소 비용만을 찾는 것이 문제이기 때문에 그리디하게 풀 수 있다.
    - 파일 합치기 시리즈 중에서 가장 쉬운 문제 (다른건 못풀겠다.......)

    - 최소 비용을 위해서 큰 장수를 최대한 나중에 합치는게 최적해가 됨
      우선 순위 큐 + 그리디
"""
