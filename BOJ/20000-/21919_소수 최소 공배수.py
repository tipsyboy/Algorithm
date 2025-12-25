import sys
from math import prod

input = sys.stdin.readline


def is_prime(target: int) -> bool:
    for i in range(2, int(target ** 0.5) + 1):
        if target % i == 0:
            return False

    return True


N = int(input())
arr = list(set(map(int, input().split())))
primes = []
for i in range(len(arr)):
    if is_prime(arr[i]):
        primes.append(arr[i])

if not primes:
    print(-1)
else:
    print(prod(primes))