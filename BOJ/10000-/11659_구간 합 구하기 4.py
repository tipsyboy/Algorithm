# https://www.acmicpc.net/problem/11659

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
psum = [0] * (N + 1)
for i in range(1, N + 1):
    psum[i] = psum[i - 1] + arr[i - 1]

for q in range(M):
    i, j = map(int, input().split())

    if i == 0:
        print(psum[j])
    else:
        print(psum[j] - psum[i - 1])
