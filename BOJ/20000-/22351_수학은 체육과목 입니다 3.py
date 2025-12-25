# 2025.03.04 TUE
# https://www.acmicpc.net/problem/22351

import sys

input = sys.stdin.readline


def solution(S):
    start_nums = [int(S[0]), int(S[:2]), int(S[:3])]

    for start in start_nums:
        cur = start
        nums = ""
        while len(S) > len(nums):
            nums += str(cur)
            if S == nums:
                return start, cur
            cur += 1

    return S, S


S = input().rstrip()
print(*solution(S))
