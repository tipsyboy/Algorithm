# 에라토스테네스의 체 + 제곱수 이용
def eratos(n):
    sieve = [False, False] + [True] * (n - 1)

    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(2 * i, n + 1, i):
                sieve[j] = False

    # prime_num = [num for num, i in enumerate(sieve) if i]
    # print(prime_num)

    ans = sieve.count(True)

    return ans


# set을 이용한 에라토스테네스의 체
def solution2(n):
    sieve = set(range(2, n + 1))

    for i in range(2, n + 1):
        if i in sieve:
            sieve -= set(range(2 * i, n + 1, i))
    return len(sieve)


eratos(10)
