# 2024.10.05 SAT
# https://www.acmicpc.net/problem/32298

import sys

input = sys.stdin.readline
MAXV = 2 * (10**6)


def is_prime(x):
    if x < 2:
        return False

    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False

    return True


def create_seq(N, M):
    for i in range(1, MAXV + 1):
        seq = list(range(i, i + (N - 1) * M + 1, M))

        if all(e <= MAXV for e in seq) and all(not is_prime(e) for e in seq):
            return seq

    return [-1]


N, M = map(int, input().split())  # 항 개수, 공차
print(*create_seq(N, M))
