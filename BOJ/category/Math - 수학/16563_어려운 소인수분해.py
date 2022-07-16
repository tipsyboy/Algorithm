import sys

input = sys.stdin.readline
MAXV = 5 * (10 ** 6)
# MAXV = 30


def get_min_prime_factor() -> list:
    min_prime_factors = [0] * (MAXV + 1)

    for i in range(MAXV + 1):
        min_prime_factors[i] = i

    for i in range(2, int(MAXV ** 0.5) + 1):
        if min_prime_factors[i] != i:
            continue

        for j in range(i + i, MAXV + 1, i):
            if min_prime_factors[j] != j:
                continue
            min_prime_factors[j] = i

    return min_prime_factors


def get_prime_factor(num: int) -> list:
    prime_factors = []

    while num > 1:
        prime_factors.append(min_prime_factors[num])
        num //= min_prime_factors[num]

    return prime_factors


N = int(input())
arr = list(map(int, input().split()))

min_prime_factors = get_min_prime_factor()
for i in range(N):
    print(*get_prime_factor(arr[i]))


"""
16563. 어려운 소인수분해
    - 1. 에라토스테네스의 체를 사용해서 소인수분해 진행 + 제곱수 전까지만 소인수 분해 확인하고,
      나머지는 자기 자신을 갖게 했음. (TLE)
    
    - 2. 1.의 아이디어를 그대로 유지하되, 소인수분해 과정에서 limit인 num**0.5가 반복되는 것을 보고
      limit 변수로 처음에만 계산함 - AC했지만 시간복잡도가 별로였음
    
    - 3. 다른 사람 코드를 보고 정수 n의 최소 소인수만을 저장해 놓는 배열을 만든 후
      거기에 대해서만 확인을 해줌 - 시간복잡도 개선
      
      포인트는 기존 에라토스테네스의 체를 사용해 단순히 소수의 여부를 판단하는 것이 아닌
      자연수 i의 최소 소수를 저장하는 아이디어.....

"""