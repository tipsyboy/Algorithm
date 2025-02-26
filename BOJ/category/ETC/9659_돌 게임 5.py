# 2025.02.19 WED
# https://www.acmicpc.net/problem/9659

import sys

input = sys.stdin.readline

N = int(input())
print("SK") if N & 1 else print("CY")
