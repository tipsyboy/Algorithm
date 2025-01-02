# 2024.12.05 THU
# https://www.acmicpc.net/problem/2891

import sys

input = sys.stdin.readline

N, S, R = map(int, input().split())

broken = set(map(int, input().split()))
extra = set(map(int, input().split()))
inter = broken & extra
broken -= inter
extra -= inter
for b in list(broken):
    if b - 1 in extra:
        broken.remove(b)
        extra.remove(b - 1)
    elif b + 1 in extra:
        broken.remove(b)
        extra.remove(b + 1)

print(len(broken))
