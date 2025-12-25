# 2024.08.19 MON
# https://www.acmicpc.net/problem/29734

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
T, S = map(int, input().split())

nq = N // 8 if N % 8 else N // 8 - 1
mq = M // 8 if M % 8 else M // 8 - 1

zip_time = N + nq * S
dok_time = M + mq * (2 * T + S) + T

if zip_time < dok_time:
    print("Zip")
    print(zip_time)
else:
    print("Dok")
    print(dok_time)
