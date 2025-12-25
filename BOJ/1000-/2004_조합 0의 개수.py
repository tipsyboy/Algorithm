# https://www.acmicpc.net/problem/2004

import sys

input = sys.stdin.readline


def get_two(x: int) -> int:
    i = 2
    two = 0
    while i <= x:
        two += x // i
        i *= 2

    return two


def get_five(x: int) -> int:
    i = 5
    five = 0
    while i <= x:
        five += x // i
        i *= 5

    return five


n, m = map(int, input().split())
five = get_five(n) - get_five(m) - get_five(n - m)
two = get_two(n) - get_two(m) - get_two(n - m)
print(min(two, five))