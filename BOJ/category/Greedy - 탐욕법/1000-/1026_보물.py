# https://www.acmicpc.net/problem/1026

import sys

input = sys.stdin.readline

N = int(input())
A = sorted(map(int, input().split()))
B = sorted(map(int, input().split()), reverse=True)

ans = 0
for a, b in zip(A, B):
    ans += a * b
print(ans)