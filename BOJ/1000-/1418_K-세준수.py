# 2025.02.10.MON
# https://www.acmicpc.net/problem/1418

import sys

input = sys.stdin.readline


def get_primes(x):
    primes = [False, False] + [True] * (x - 1)

    for i in range(2, int(x**0.5) + 1):
        if primes[i]:
            for j in range(i + i, x + 1, i):
                primes[j] = False

    return primes


N = int(input())
K = int(input())

primes = get_primes(N)

ans = [0] + [1] * N
for t in range(K + 1, N + 1):
    if primes[t] and t > K:
        for i in range(t, N + 1, t):
            ans[i] = 0

print(sum(ans))

# 1. 타겟 범위 -> K보다 작은 수들을 K보다 작은 소인수를 갖는다.
# 2. 어떤 소수 t의 배수들은 t를 소인수를 갖는다.
# 3. 2.의 의해 소수 t의 배수중 K보다 큰 수들에 대해서 제거해줘야한다.
