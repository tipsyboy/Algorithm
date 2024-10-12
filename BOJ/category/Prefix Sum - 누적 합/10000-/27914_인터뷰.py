# 2024.10.07 MON
# https://www.acmicpc.net/problem/27914

import sys

input = sys.stdin.readline

N, K, Q = map(int, input().split())
A = list(map(int, input().split()))
X = list(map(int, input().split()))

psum = [0]
length = 0
for i in range(N):
    length += 1
    if A[i] == K:
        length = 0

    psum.append(psum[-1] + length)

for q in X:
    print(psum[q])
