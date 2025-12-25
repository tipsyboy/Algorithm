# https://www.acmicpc.net/problem/19951

import sys

input = sys.stdin.readline


N, M = map(int, input().split())
ground_init = list(map(int, input().split()))

ground = [0] * (N + 1)
for _ in range(M):
    a, b, k = map(int, input().split())
    ground[a - 1] += k
    ground[b] -= k

for i in range(1, N):
    ground[i] += ground[i - 1]

for i in range(N):
    ground_init[i] += ground[i]

print(*ground_init)


"""
19951. 태상이의 훈련소 생활
    - 누적 합 문제
    - imos법을 알게되고 다시 공부하면서 풀게됨.
"""