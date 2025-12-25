# 2024.07.17 WED
# https://www.acmicpc.net/problem/31927

import sys

input = sys.stdin.readline
MAX_A = 5000
MAX_x = 10**6

N = int(input())
A = list(map(int, input().split()))
print(N // 2)
for i in range(N // 2):
    A[i] += MAX_x - MAX_A * i
    A[N - i - 1] -= MAX_x - MAX_A * i
    print(*A)
