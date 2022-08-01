import sys

input = sys.stdin.readline


def get_candidate_numbers(picked: list, depth: int, K: int, num: int) -> None:
    global candidate_nums

    if depth == K:
        candidate_nums.append(num)
        return

    for i in range(10):
        if (depth == K - 1 and i == 0) or picked[i]:
            continue

        picked[i] = True
        num += i * (10 ** depth)
        get_candidate_numbers(picked, depth + 1, K, num)
        num -= i * (10 ** depth)
        picked[i] = False


def get_prime_numbers(K: int) -> list:
    MAXV = 10 ** K
    sieve = [False, False] + [True] * (MAXV - 1)

    for i in range(2, int(MAXV ** 0.5) + 1):
        if not sieve[i]:
            continue

        for j in range(i + i, MAXV + 1, i):
            if sieve[j]:
                sieve[j] = False

    return sieve


def condition1(target: int) -> bool:
    for i in range(2, target // 2 + 1):
        if sieve[i] and sieve[target - i] and i != target - i:
            return True

    return False


def condition2(target: int, M: int) -> bool:
    while target % M == 0:
        target //= M

    for i in range(2, int(target ** 0.5) + 1):
        if target % i == 0 and sieve[i] and sieve[target // i]:
            return True

    return False


K, M = map(int, input().split())
sieve = get_prime_numbers(K)

picked = [False] * 10
candidate_nums = []
get_candidate_numbers(picked, 0, K, 0)
cnt = 0
for target in candidate_nums:
    if condition1(target) and condition2(target, M):
        cnt += 1
print(cnt)


"""
22943. 수
    - 조건에 맞게 하나하나씩 구현하면 되지만 들어가는 개념이 3~4개가 나온다. 실버는 절대 아니라고 생각함.

    - 1, 2 조건에 따라서 풀이 
"""