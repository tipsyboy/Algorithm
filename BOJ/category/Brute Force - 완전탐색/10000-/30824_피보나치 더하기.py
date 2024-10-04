# 2024.09.30 MON
# https://www.acmicpc.net/problem/30824

import sys

input = sys.stdin.readline
MAXV = 10**16


def get_fibo_seq(lim):
    seq = [1, 1]
    while seq[-1] < lim:
        seq.append(seq[-1] + seq[-2])

    return seq


def binary_search(target, fibo_seq):
    lo, hi = 0, len(fibo_seq)

    while lo <= hi:

        mid = (lo + hi) // 2
        if fibo_seq[mid] <= target:
            lo = mid + 1
        else:
            hi = mid - 1
    return fibo_seq[hi]


fibo_seq = get_fibo_seq(MAXV)
T = int(input())
for _ in range(T):
    k, x = map(int, input().split())

    if k > x:
        print("NO")
        continue

    for i in range(k):
        if x == 0:
            break
        x -= binary_search(x, fibo_seq)

    if x == 0:
        print("YES")
    else:
        print("NO")
