# https://www.acmicpc.net/problem/1929

import sys

input = sys.stdin.readline


def eratosthenes_sieve(N: int) -> list:
    sieve = [False, False] + [True] * (N - 1)

    for i in range(2, int(N ** 0.5) + 1):
        if not sieve[i]:
            continue

        for j in range(i + i, N + 1, i):
            sieve[j] = False

    return sieve


M, N = map(int, input().split())

sieve = eratosthenes_sieve(N)
for i in range(M, N + 1):
    if sieve[i]:
        print(i)