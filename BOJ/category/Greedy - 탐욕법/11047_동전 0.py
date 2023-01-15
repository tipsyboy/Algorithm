# https://www.acmicpc.net/problem/11047

import sys

input = sys.stdin.readline

N, K = map(int, input().split())
coins = []
for _ in range(N):
    coins.append(int(input()))

ans = 0
for i in range(N - 1, 0, -1):
    ans += K // coins[i]
    K %= coins[i]

print(ans + K)  # K: 마지막 1원 남은 수
