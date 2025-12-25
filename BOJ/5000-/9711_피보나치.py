# 2025.01.03 FRI
# https://www.acmicpc.net/problem/9711

import sys

input = sys.stdin.readline

T = int(input())
fibo = [0, 1, 1]
for i in range(10000):
    fibo.append(fibo[-1] + fibo[-2])
for i in range(1, T + 1):
    P, Q = map(int, input().split())
    print(f"Case #{i}: {fibo[P]%Q}")
