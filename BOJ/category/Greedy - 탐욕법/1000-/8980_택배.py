# https://www.acmicpc.net/problem/8980

import sys

input = sys.stdin.readline

N, C = map(int, input().split())
M = int(input())
delivery = []
for _ in range(M):
    u, v, box = map(int, input().split())
    delivery.append((u, v, box))

delivery.sort(key=lambda x: x[1])
capacity = [C] * (N + 1)
ans = 0
for u, v, box in delivery:
    possible = C
    for i in range(u, v):
        temp = min(capacity[i], box)
        if possible >= temp:
            possible = min(capacity[i], box)

    for i in range(u, v):
        capacity[i] -= possible
    ans += possible

print(ans)


"""
8980. 택배
    - 트럭의 최대 용량이 C이므로 뒤에 더 많이 실을 수 있는 마을이 있더라도 먼저 내려 놓는 것이 이득이다.
      따라서 도착지를 오름차순해서 정렬한다. 
      
    - 구간 [u, v) 에서 적재할 수 있는 택배의 양을 생각한다. 
"""