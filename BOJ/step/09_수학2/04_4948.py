import sys

# 에라토스테네스의 체 1부터 N까지의 소수 구하기


def Eratos(N):
    primes = [False, False] + [True] * (N-1)  # 체 생성

    for i in range(2, int(N**0.5)+1):  # 제곱근까지 검증
        if primes[i]:
            for j in range(2*i, N+1, i):
                primes[j] = False

    return primes


# 미리 에라토스테네스의 체로 범위까지 소수 배열을 찾는다.
primes = Eratos(123456 * 2)
while True:
    input_num = int(sys.stdin.readline())

    if input_num == 0:
        break

    print(primes[input_num+1: 2*input_num+1].count(True))
    # cnt = 0
    # for i in range(input_num + 1, 2*input_num + 1):
    #     if primes[i]:
    #         cnt += 1

    # print(cnt)
