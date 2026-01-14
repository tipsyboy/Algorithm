# Jun 12, 2025 Thu
# https://www.acmicpc.net/problem/14490

import sys

input = sys.stdin.readline


def gcd(a, b):
    while b:
        r = a % b
        a = b
        b = r

    return a


st = input().split(":")
a, b = map(int, st)
d = gcd(a, b)
print(f"{a//d}:{b//d}")
