# https://www.acmicpc.net/problem/11005

import sys

input = sys.stdin.readline
T = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def convert_num_system(n: int, base: int) -> str:
    q, r = divmod(n, base)

    return convert_num_system(q, base) + T[r] if q else T[r]


N, B = map(int, input().split())
print(convert_num_system(N, B))