import sys
from math import sqrt  # 루트


# 1번_모든 수를 전부 검사하는 방법
def is_Prime_1(num):
    if num == 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


# 2번_루트를 활용하는 방법
def is_Prime_2(num):
    if num == 1:
        return False

    x = int(sqrt(num))

    for i in range(2, x+1):
        if num % i == 0:
            return False

    return True


M = int(sys.stdin.readline())
N = int(sys.stdin.readline())

prime_list = []

for number in range(M, N+1):
    if is_Prime_2(number):
        prime_list.append(number)

if len(prime_list) == 0:
    print(-1)
else:
    print(sum(prime_list))
    print(min(prime_list))
