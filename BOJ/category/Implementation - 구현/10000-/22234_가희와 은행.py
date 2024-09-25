# 2024.09.21 SAT
# https://www.acmicpc.net/problem/22234

import sys
from collections import deque

input = sys.stdin.readline

N, T, W = map(int, input().split())
q = deque()
for _ in range(N):
    P, t = map(int, input().split())
    q.append((P, t))

M = int(input())
after = []
for _ in range(M):
    P, t, c = map(int, input().split())
    after.append((P, t, c))
after.sort(key=lambda x: -x[2])

ans = []
time = 0
while time < W:
    P, t = q.popleft()

    if t > T:
        ans.extend([P] * min((W - time), T))
        time += T
    else:
        ans.extend([P] * min((W - time), t))
        time += t

    while after and after[-1][2] <= time:
        af_id, af_tx, _ = after.pop()
        q.append((af_id, af_tx))

    if t > T:
        q.append((P, t - T))

print(*ans, sep="\n")
