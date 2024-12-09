# 2024.11.24 SUN
# https://www.acmicpc.net/problem/25185


import sys
from itertools import combinations

input = sys.stdin.readline


def condition1(cards):
    L = len(cards)
    for x, y, z in combinations(range(L), 3):
        n1, a1 = int(cards[x][0]), cards[x][1]
        n2, a2 = int(cards[y][0]), cards[y][1]
        n3, a3 = int(cards[z][0]), cards[z][1]
        nums = [n1, n2, n3]
        if a1 == a2 == a3:
            nums.sort()
            if nums[0] + 2 == nums[1] + 1 == nums[2]:
                return True

    return False


def condition2(cards):
    a, b, c, d = cards
    return (a == b == c) or (a == b == d) or (a == c == d) or (b == c == d)


def condition3(cards):
    a, b, c, d = cards
    return (a == b and c == d) or (a == c and b == d) or (a == d and b == c)


T = int(input())
ans = []
for _ in range(T):
    cards = input().split()

    if condition1(cards) or condition2(cards) or condition3(cards):
        ans.append(":)")
    else:
        ans.append(":(")

print(*ans, sep="\n")
