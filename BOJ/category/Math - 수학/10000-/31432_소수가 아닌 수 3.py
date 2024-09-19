# 2024.09.11 WED
# https://www.acmicpc.net/problem/31432

import sys

input = sys.stdin.readline


"""
31432. 소수가 아닌 수 3
- 111 = 3 * 37 으로 합성수기 때문에 solution2()로 풀 수 있음.
"""


def solution2(N, numbers):
    return f"YES\n{int(numbers[0]) * 111}"


def is_prime(number):
    if number < 2:
        return False

    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False

    return True


def make_number(number, digit, d):
    global ans

    if ans != None:
        return

    if digit == d:
        if not is_prime(int(number)):
            ans = int(number)
        return

    for num in numbers:
        make_number(number + num, digit + 1, d)


N = int(input())
numbers = list(input().split())

ans = None
for d in range(1, 12):
    if ans != None:
        break
    make_number("", 0, d)

if ans == None:
    print("NO")
else:
    print("YES")
    print(ans)

print(solution2(N, numbers))
