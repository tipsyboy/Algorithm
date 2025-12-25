# 2024.09.03 TUE
# https://www.acmicpc.net/problem/31964

import sys

input = sys.stdin.readline

N = int(input())
X = list(map(int, input().split()))  # 집의 위치
T = list(map(int, input().split()))  # 택배를 내려놓는 시간

time = X[N - 1]
for i in range(N - 1, -1, -1):
    if i != N - 1:
        time += X[i + 1] - X[i]
    if T[i] > time:
        time += T[i] - time
time += X[0]

print(time)
