# https://www.acmicpc.net/problem/1015

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

num_posi = dict()
for idx, elem in enumerate(sorted(A)):
    if elem not in num_posi:
        num_posi[elem] = deque()

    num_posi[elem].append(idx)

P = [0] * N
for idx, elem in enumerate(A):
    P[idx] = num_posi[elem].popleft()
print(*P)
