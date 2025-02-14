# 2025.01.28 TUE
# https://www.acmicpc.net/problem/32653

import sys

from math import lcm

N = int(input())
X = list(map(int, input().split()))
l = lcm(*X)

while not all((l // x) % 2 == 0 for x in X):
    l *= 2

print(l)
