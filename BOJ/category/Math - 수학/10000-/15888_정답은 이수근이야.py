# # 2024.08.09 FRI
# https://www.acmicpc.net/problem/15888

import sys

input = sys.stdin.readline


def is_power_of_two(x):
    return x > 1 and (x & (x - 1)) == 0


def lee_soo_geun(A, B, C):
    D = B * B - 4 * A * C
    if D <= 0:
        return "둘다틀렸근"

    n = (-B + (B**2 - 4 * A * C) ** 0.5) / (2 * A)
    m = (-B - (B**2 - 4 * A * C) ** 0.5) / (2 * A)

    if is_power_of_two(int(n)) and is_power_of_two(int(m)):
        return "이수근"

    if int(n) == n and int(m) == m:
        return "정수근"

    return "둘다틀렸근"


A, B, C = map(int, input().split())
print(lee_soo_geun(A, B, C))
