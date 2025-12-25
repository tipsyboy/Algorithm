# 2025.03.02 SUN
# https://www.acmicpc.net/problem/28136

import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.append(arr[0])
cnt = 0
for i in range(N):
    if arr[i] >= arr[i + 1]:
        cnt += 1
print(cnt)
