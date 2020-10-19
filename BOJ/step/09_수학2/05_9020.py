import sys


# Sieve of Eratosthenes
def Eratos(rng):
    # if rng <= 1:
    #     return
    primes = [False, False] + [True] * (rng-1)  # 체 생성

    for i in range(2, int(rng**0.5)+1):
        if primes[i]:
            for j in range(2*i, rng+1, i):
                primes[j] = False

    return primes


#
t_case = int(sys.stdin.readline())
primes = Eratos(10000)  # 소수 구하기

for i in range(t_case):
    n = int(sys.stdin.readline())  # 짝수 n 입력

    # 골드바흐 수 찾기
    # 몫: 자연수
    for j in range(n//2, 1, -1):
        if primes[j] and primes[n-j]:
            print(j, n-j)
            break
