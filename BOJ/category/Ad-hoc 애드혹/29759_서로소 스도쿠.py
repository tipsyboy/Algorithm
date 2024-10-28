# 2024.10.21 MON
# https://www.acmicpc.net/problem/29759

import sys

input = sys.stdin.readline
MAXV = 110_000


def eratos():
    for i in range(2, int(MAXV**0.5) + 1):
        if not sieve[i]:
            continue

        for j in range(i + i, MAXV + 1, i):
            if sieve[j]:
                sieve[j] = False


def remove_divider(x):
    for i in range(1, min(MAXV, int(x**0.5)) + 1):
        if x % i == 0:
            sieve[i] = False
            if x // i <= MAXV:
                sieve[x // i] = False


N = int(input())
N2 = N**2
grid = [list(map(int, input().split())) for _ in range(N2)]

sieve = [True] * (MAXV + 1)
sieve[0] = sieve[1] = False

eratos()
for i in range(N2):
    for j in range(N2):
        if grid[i][j] != 0:
            remove_divider(grid[i][j])

primes = []
for i in range(2, MAXV + 1):
    if sieve[i]:
        primes.append(i)


for i in range(N2):
    for j in range(N2):
        if grid[i][j] == 0:
            grid[i][j] = primes.pop()

for i in range(N2):
    print(*grid[i])
