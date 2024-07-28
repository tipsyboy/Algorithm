# 2024.07.24 WED
# https://www.acmicpc.net/problem/14677

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline
PILL_ORDER = ["B", "L", "D"]


def bt(cur, state):
    cur_order = PILL_ORDER[cur]
    if len(state) == 0 or (state[0] != cur_order and state[-1] != cur_order):
        return 3 * N - len(state)

    if state in dp:
        return dp[state]

    nxt = (cur + 1) % 3
    if cur_order == state[0]:
        dp[state] = max(dp.get(state, 0), bt(nxt, state[1:]))
    if cur_order == state[-1]:
        dp[state] = max(dp.get(state, 0), bt(nxt, state[:-1]))

    return dp[state]


N = int(input())
pills = input().rstrip()
dp = dict()
bt(0, pills)
print(dp.get(pills, 0))
