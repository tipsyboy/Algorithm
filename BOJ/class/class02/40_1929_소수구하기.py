import sys

input = sys.stdin.readline

n, m = map(int, input().split())
eratos_sieve = [False, False] + [True] * (m - 1)

for i in range(2, int(m ** 0.5) + 1):
    if eratos_sieve[i]:
        for j in range(2 * i, m + 1, i):
            eratos_sieve[j] = False

for i in range(n, m + 1):
    if eratos_sieve[i]:
        print(i)
