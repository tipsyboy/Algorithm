# 2025.02.17 MON
# https://www.acmicpc.net/problem/2057

"""
2057. 팩토리얼 분해

- N! >= (N-1)! + (N-2)! + ... + 1! + 0!
"""

import sys

input = sys.stdin.readline


def get_factorial_nums(N):
    factorials = [1]
    x = 1
    while factorials[-1] < N:
        factorials.append(factorials[-1] * x)
        x += 1
    return factorials


N = int(input())
ans = "NO"
if N != 0:
    factorials = get_factorial_nums(N)
    for i in range(len(factorials) - 1, -1, -1):
        if factorials[i] <= N:
            N -= factorials[i]
    if N == 0:
        ans = "YES"
print(ans)
