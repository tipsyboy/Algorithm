# 2024.11.04 MON
# https://www.acmicpc.net/problem/19949

import sys

input = sys.stdin.readline


def solution1():
    def pick(num, picked, correct):
        nonlocal ans

        if correct < num - 5:
            return

        if num == 10:
            if correct >= 5:
                ans += 1
            return

        for i in range(1, 6):
            if num >= 2 and i == picked[-1] == picked[-2]:
                continue

            c = int(i == answer[num])
            picked.append(i)
            pick(num + 1, picked, correct + c)
            picked.pop()

    answer = list(map(int, input().split()))
    ans = 0
    pick(0, [], 0)

    return ans


def solution2():
    def pick(num, p1, p2, score):
        if score < num - 5:
            return 0

        if num == 10:
            return 1

        if dp[num][p1][p2][score] != -1:
            return dp[num][p1][p2][score]

        rst = 0
        for i in range(1, 6):
            if p1 == p2 == i:
                continue

            correct = int(i == answer[num])
            rst += pick(num + 1, p2, i, score + correct)

        dp[num][p1][p2][score] = rst
        return rst

    answer = list(map(int, input().split()))
    dp = [[[[-1] * 11 for _ in range(6)] for __ in range(6)] for ___ in range(11)]
    return pick(0, 0, 0, 0)


print(solution1())
print(solution2())
