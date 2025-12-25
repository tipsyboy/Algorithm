# 2024.07.27 SAT
# https://www.acmicpc.net/problem/28286

import sys

input = sys.stdin.readline


def pull(p, state):
    return state[:p] + state[p + 1 :] + [0]


def push(p, state):
    return (state[:p] + [0] + state[p:])[:-1]


def check(state):
    cnt = 0
    for i in range(N):
        if state[i] == answer[i]:
            cnt += 1
    return cnt


def dfs(lv, state):
    global ans

    ans = max(ans, check(state))

    if lv == K:
        return

    for p in range(N):
        push_state = push(p, state)
        pull_state = pull(p, state)
        dfs(lv + 1, push_state)
        dfs(lv + 1, pull_state)


N, K = map(int, input().split())
answer = list(map(int, input().split()))
omr = list(map(int, input().split()))

ans = check(omr)
dfs(0, omr)
print(ans)
