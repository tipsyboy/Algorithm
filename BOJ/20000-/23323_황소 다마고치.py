# 2024.07.28 SUN
# https://www.acmicpc.net/problem/23323

import sys
from math import log2

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    print(int(log2(n)) + m + 1)
