# 2024.10.12 SAT
# https://www.acmicpc.net/problem/9656

import sys

input = sys.stdin.readline

N = int(input())
print("CY") if N & 1 else print("SK")
