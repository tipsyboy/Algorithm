# 2024.12.23 MON
# https://www.acmicpc.net/problem/2885

import sys

input = sys.stdin.readline

K = int(input())

mn = 0
while K > (1 << mn):
    mn += 1

d = 0
while not K & (1 << d):
    d += 1

print(1 << mn, mn - d)
