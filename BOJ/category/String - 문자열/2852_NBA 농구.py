# https://www.acmicpc.net/problem/2852

import sys

input = sys.stdin.readline


def make_time(sec: int) -> str:
    m, s = sec // 60, sec % 60
    return str(m).zfill(2) + ":" + str(s).zfill(2)


def cal_win_time(score: list, now: int, prev: int) -> None:
    if score[0] > score[1]:
        ans[0] += now - prev
    elif score[0] < score[1]:
        ans[1] += now - prev


N = int(input())
score = [0, 0]
ans = [0, 0]
prev = 0
for _ in range(N):
    team, time = input().split()

    m, s = time.split(":")
    now = int(m) * 60 + int(s)

    cal_win_time(score, now, prev)

    prev = now
    score[int(team) - 1] += 2


now = 2880
cal_win_time(score, now, prev)

print(make_time(ans[0]))
print(make_time(ans[1]))