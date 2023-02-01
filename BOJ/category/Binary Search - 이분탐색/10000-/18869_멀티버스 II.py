# https://www.acmicpc.net/problem/18869

import sys
from bisect import bisect_left

input = sys.stdin.readline


def compare_planet_size(universe: list) -> list:
    dedupulicted = sorted(set(universe))

    rst = []
    for i in range(len(universe)):
        rst.append(bisect_left(dedupulicted, universe[i]))

    return rst


M, N = map(int, input().split())
universes = []
for _ in range(M):
    universes.append(list(map(int, input().split())))

eq = []
for i in range(M):
    eq.append(compare_planet_size(universes[i]))

ans = 0
for i in range(M - 1):
    for j in range(i + 1, M):
        if eq[i] == eq[j]:
            ans += 1

print(ans)