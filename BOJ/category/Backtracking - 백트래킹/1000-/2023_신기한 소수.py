# 2024.10.26 SAT
# https://www.acmicpc.net/problem/2023


import sys

input = sys.stdin.readline


def is_prime(x):
    if x < 2:
        return False

    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False

    return True


def dfs(d, num):
    if d == N:
        print(num)
        return

    nxt = num * 10
    for i in range(1, 10):
        if is_prime(nxt + i):
            dfs(d + 1, nxt + i)


N = int(input())
dfs(0, 0)
