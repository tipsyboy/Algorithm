# Dec 10, Wed 2025
# https://www.acmicpc.net/problem/9037

import sys

input = sys.stdin.readline


def make_even(candies):
    even_candies = []
    for candy in candies:
        even_candies.append(candy + 1 if candy & 1 else candy)
    return even_candies


T = int(input())
for _ in range(T):
    N = int(input())
    candies = list(map(int, input().split()))
    candies = make_even(candies)

    cycle = 0
    while not all(candy == candies[0] for candy in candies):
        nxt = [0] * N
        for i, candy in enumerate(candies):
            nxt[i] = candy // 2 + candies[(i - 1) % N] // 2
        candies = make_even(nxt)
        cycle += 1
    print(cycle)
