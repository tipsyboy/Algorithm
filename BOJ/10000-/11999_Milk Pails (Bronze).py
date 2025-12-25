# https://www.acmicpc.net/problem/11999

import sys

input = sys.stdin.readline

X, Y, M = map(int, input().split())
a = 0
ans, min_r = 0, float("inf")
while M >= X * a:
    r = (M - X * a) % Y
    if r < min_r:
        ans = M - r
        min_r = r
    a += 1
print(ans)
