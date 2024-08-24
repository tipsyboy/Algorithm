# 2024.08.21 WED
# https://www.acmicpc.net/problem/27922

import sys

input = sys.stdin.readline

N, K = map(int, input().split())
ab, bc, ac = [], [], []
for _ in range(N):
    a, b, c = map(int, input().split())
    ab.append(a + b)
    bc.append(b + c)
    ac.append(a + c)

ab.sort(reverse=True)
bc.sort(reverse=True)
ac.sort(reverse=True)

print(max(sum(ab[:K]), sum(bc[:K]), sum(ac[:K])))
