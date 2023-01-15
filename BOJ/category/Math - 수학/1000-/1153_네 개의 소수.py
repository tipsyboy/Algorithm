import sys

input = sys.stdin.readline


def eratos(N: int) -> list:
    sieve = [False, False] + [True] * (N - 1)

    for i in range(2, int(N ** 0.5)):
        if not sieve[i]:
            continue

        for j in range(i + i, N + 1, i):
            sieve[j] = False

    return sieve


def solution(N: int) -> list:
    if N < 8:  # 4개의 소수 합으로 나타낼 수 없음
        return [-1]

    sieve = eratos(N)
    if N % 2 == 0:
        ans = [2, 2]
        N -= 4
    else:
        ans = [2, 3]
        N -= 5

    # 골드바흐의 추측을 이용한다.
    flag = False
    for i in range(2, N // 2 + 1):
        if sieve[i] and sieve[N - i]:
            flag = True
            ans.append(i)
            ans.append(N - i)
            break

    if not flag:
        ans = [-1]
    return ans


N = int(input())
print(*solution(N))


"""
1153. 네 개의 소수
    1. 문제가 물어보는 것
    - 자연수 N에 대해 4개의 소수의 합으로 나타내는 방법

    1-1. 포인트
    - 우리가 알고 있는 가장 작은 소수인 2와 3을 이용한다. 

    2. 필요 알고리즘 개념
    - 알고리즘 개념이라기보단 에라토스테네스의 체와 골드바흐의 추측이 필요함

    3. 풀이
    - 골드바흐의 추측은 증명되진 않았지만, 문제의 N의 범위 내에서는 입증 되었음.
      이를 이용해서 N을 우리가 알고 있는 소수중 가장 작은 수인 2와 3을 이용해 2개의 소수합을 만드는 동시에 
      나머지 두 소수를 구하기 위해 짝수로 만들어줌 (N이 짝수인 경우 2, 2를 사용해서 짝수로, 홀수인 경우 2, 3을 사용해서 짝수로)

      이제, 남은 수에 대해서 에라토스테네스의 체를 사용해서 알맞은 소수쌍을 찾아주면 된다. 
"""