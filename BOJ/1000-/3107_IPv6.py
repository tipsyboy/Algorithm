# Dec 6, Sat 2025
# https://www.acmicpc.net/problem/3107

import sys

input = sys.stdin.readline


def fill_zero(arr):
    rst = []
    for e in arr:
        if e == "":
            continue
        rst.append(e.zfill(4))
    return ":".join(rst)


def solution(ipv6):
    if "::" not in ipv6:
        addr_arr = ipv6.split(":")
        return fill_zero(addr_arr)

    left, right = ipv6.split("::")
    left = left.split(":") if left else []
    right = right.split(":") if right else []
    zero_group = ["0000"] * (8 - (len(left) + len(right)))
    return fill_zero(left + zero_group + right)


ipv6 = input().rstrip()
print(solution(ipv6))
