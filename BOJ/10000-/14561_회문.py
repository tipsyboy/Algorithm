# 2024.10.01 TUE
# https://www.acmicpc.net/problem/14561

import sys

input = sys.stdin.readline


def convert_number_system(num, base):
    B = "0123456789ABCDEF"  # n <= 16

    q, r = divmod(num, base)

    return convert_number_system(q, base) + B[r] if q else B[r]


def is_palindrome(x):
    return x == x[::-1]


T = int(input())
for _ in range(T):
    A, n = map(int, input().split())

    base_num = convert_number_system(A, n)
    print(1) if is_palindrome(base_num) else print(0)
