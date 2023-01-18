# https://www.acmicpc.net/problem/10816

import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline


def sol1() -> list:
    ans = []

    for t in arr:
        ans.append(str(bisect_right(cards, t) - bisect_left(cards, t)))

    return ans


def left_idx(target: int, cards: list) -> int:
    lo, hi = 0, len(cards)

    while lo < hi:
        mid = (lo + hi) // 2

        if target <= cards[mid]:
            hi = mid
        else:
            lo = mid + 1

    return lo


def right_idx(target: int, cards: list):
    lo, hi = 0, len(cards)

    while lo < hi:
        mid = (lo + hi) // 2

        if target < cards[mid]:
            hi = mid
        else:
            lo = mid + 1

    return lo


def sol2() -> list:
    ans = []
    for t in arr:
        ans.append(str(right_idx(t, cards) - left_idx(t, cards)))

    return ans


N = int(input())
cards = sorted(map(int, input().split()))
M = int(input())
arr = list(map(int, input().split()))

# print(" ".join(sol1()))
print(" ".join(sol2()))
