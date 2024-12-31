# 2024.12.24 TUE
# https://www.acmicpc.net/problem/1684

import sys
from math import gcd

input = sys.stdin.readline


n = int(input())
arr = list(map(int, input().split()))

diffs = []
for i in range(n - 1):
    for j in range(i + 1, n):
        diffs.append(abs(arr[i] - arr[j]))

print(gcd(*diffs))
