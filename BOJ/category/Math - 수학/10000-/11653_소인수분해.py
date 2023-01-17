# https://www.acmicpc.net/problem/11653

import sys

input = sys.stdin.readline


def pf(N: int) -> list:
    primes = []

    for i in range(2, int(N ** 0.5) + 1):
        while N % i == 0:
            primes.append(i)
            N //= i

    if N != 1:
        primes.append(N)

    return primes


N = int(input())
print(*pf(N), sep="\n")
