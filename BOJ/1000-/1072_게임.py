# https://www.acmicpc.net/problem/1072

import sys

input = sys.stdin.readline
MAXV = 1_000_000_000


def sol(X: int, Y: int, Z: int) -> int:
    if X == Y:
        return -1

    ans = -1
    lo, hi = 1, MAXV
    while lo <= hi:
        mid = (lo + hi) // 2

        if (Y + mid) * 100 // (X + mid) > Z:
            ans = mid
            hi = mid - 1
        else:
            lo = mid + 1

    return ans


X, Y = map(int, input().split())
Z = Y * 100 // X
print(sol(X, Y, Z))