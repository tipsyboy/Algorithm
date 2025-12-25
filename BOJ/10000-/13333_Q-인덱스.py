# https://www.acmicpc.net/problem/13333

import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

k = 0
for i in range(n, -1, -1):
    cnt = 0
    for e in arr:
        if e >= i:
            cnt += 1
    if cnt >= i:
        k = i
        break
print(k)