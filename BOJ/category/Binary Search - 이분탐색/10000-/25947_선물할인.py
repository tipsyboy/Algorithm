# 2024.07.15 MON
# https://www.acmicpc.net/problem/25947

import sys

input = sys.stdin.readline


def search(lo, hi):
    if lo > hi:
        return hi

    mid = (lo + hi) // 2
    total = psum[mid]
    for i in range(min(mid, a)):
        total -= prices[mid - 1 - i] // 2

    if total <= b:
        return search(mid + 1, hi)
    else:
        return search(lo, mid - 1)


n, b, a = map(int, input().split())
prices = list(map(int, input().split()))
prices.sort()
psum = [0]
for i in range(n):
    psum.append(psum[-1] + prices[i])

print(search(0, n))
