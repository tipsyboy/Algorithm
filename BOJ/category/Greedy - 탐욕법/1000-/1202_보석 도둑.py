# https://www.acmicpc.net/problem/1202

import sys
from heapq import heappush, heappop

input = sys.stdin.readline


N, K = map(int, input().split())
jewelry, bags = [], []
for _ in range(N):
    M, V = map(int, input().split())
    heappush(jewelry, (M, -V))
for _ in range(K):
    bags.append(int(input()))

bags.sort()
ans = 0
candidates = []
for bag in bags:
    while jewelry and bag >= jewelry[0][0]:
        heappush(candidates, jewelry[0][1])
        heappop(jewelry)

    if candidates:
        ans += heappop(candidates)

    if not candidates and not jewelry:
        break


print(-ans)


"""
1202. 보석 도둑
    1.모든 가방을 B, i번째 가방을 Bi라고 할때 가방 B를 정렬하고 매번 가방 Bi마다 들어 갈 수 있는 모든 
      보석을 훔칠 수 있는 후보군 C로 둔다.

    2.가방 B는 오름 차순으로 정렬되어 있으므로 필연적으로 후보군에 들은 보석 C들은 Bi+1에 들어 갈 수 있다.
    
    3. 이후 가방마다 가장 가치가 높은 보석을 넣는다.
    
      

"""