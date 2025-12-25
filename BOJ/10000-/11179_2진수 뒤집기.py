# https://www.acmicpc.net/problem/11179

import sys

input = sys.stdin.readline


def convert_dec2bin(num: int) -> str:
    T = "01"
    q, r = divmod(num, 2)

    return convert_dec2bin(q) + T[r] if q else T[r]


N = int(input())
print(int(convert_dec2bin(N)[::-1], 2))
