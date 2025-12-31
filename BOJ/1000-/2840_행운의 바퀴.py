# Dec 17, Wed 2025
# https://www.acmicpc.net/problem/2840

import sys

input = sys.stdin.readline


def solution(N, K):
    roulette = ["?"] * N
    pos = 0

    for _ in range(K):
        S, char = input().split()
        pos = (pos + int(S)) % N

        if roulette[pos] != "?" and roulette[pos] != char:
            return "!"

        roulette[pos] = char

    chars = [c for c in roulette if c != "?"]
    if len(chars) != len(set(chars)):
        return "!"

    return "".join(roulette[pos::-1] + roulette[N - 1 : pos : -1])


N, K = map(int, input().split())
print(solution(N, K))
