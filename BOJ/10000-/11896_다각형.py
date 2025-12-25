# 2024.07.25 THU
# https://www.acmicpc.net/problem/11896

import sys

input = sys.stdin.readline

a, b = map(int, input().split())

s = a + a % 2
e = b - b % 2
if s < 3:
    s = 4

if s > e:
    print(0)
else:
    t = (e - s) // 2 + 1
    print(t * (s + e) // 2)
