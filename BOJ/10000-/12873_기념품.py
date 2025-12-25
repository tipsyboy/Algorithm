# https://www.acmicpc.net/problem/12873

"""
12873. 기념품
    1. 파이썬 deque의 rotate를 쓰는 방법
    2. N <= 5000 이므로 리스트 pop()으로 O(N^2)으로 해도 TLE가 아님
"""

import sys

input = sys.stdin.readline

N = int(input())
A = [i for i in range(1, N + 1)]

p, t = 0, 1
while len(A) > 1:
    t3 = t ** 3

    move = t3 % len(A) - 1
    p = (p + move) % len(A)
    A.pop(p)

    t += 1

print(*A)
