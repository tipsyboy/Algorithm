# https://www.acmicpc.net/problem/1484
# 2022-08-08 MON

import sys

input = sys.stdin.readline


def search(G: int) -> list:
    lo, hi = 1, 2
    ans = []
    while lo < hi and hi < G + 1:
        temp = hi ** 2 - lo ** 2

        if temp == G:
            ans.append(hi)
            lo += 1
            hi += 1
        elif temp > G:
            lo += 1
        else:
            hi += 1

    return [-1] if not ans else ans


G = int(input())
print(*search(G), sep="\n")


"""
1484. 다이어트
    1. 반복의 범위에 대해서 잘 생각해야함.

    2. G = x^2 - y^2 (x: 현재 몸무게, y: 기억하는 몸무게)
    이므로 G = (x-y)(x+y)의 순서쌍을 찾아 준다. 
"""