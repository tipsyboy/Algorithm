# 2024.11.07 THU
# https://www.acmicpc.net/problem/25375

import sys

input = sys.stdin.readline

Q = int(input())
for _ in range(Q):
    a, b = map(int, input().split())

    print(1) if a != b and b % a == 0 else print(0)
