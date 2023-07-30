# https://www.acmicpc.net/problem/4375

"""
4375. 1
    - 처음에 뭔소린지 몰라서 조금 해맸음
"""


def sol(n: int) -> int:
    x = 1
    while True:
        if x % n == 0:
            break
        x = x * 10 + 1

    return len(str(x))


while True:
    try:
        n = int(input())
    except EOFError:
        break

    print(sol(n))