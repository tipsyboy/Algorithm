# https://www.acmicpc.net/problem/14491

import sys

input = sys.stdin.readline


def convert_num_system(num: int, base: int) -> str:
    T = "012345678"
    q, r = divmod(num, base)

    return convert_num_system(q, base) + T[r] if q else T[r]


T = int(input())
print(convert_num_system(T, 9))
