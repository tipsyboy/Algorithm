# 2024.09.16 MON
# https://www.acmicpc.net/problem/32306

import sys

input = sys.stdin.readline

team1 = list(map(int, input().split()))
team2 = list(map(int, input().split()))

score_team1 = team1[0] + team1[1] * 2 + team1[2] * 3
score_team2 = team2[0] + team2[1] * 2 + team2[2] * 3

if score_team1 == score_team2:
    print(0)
elif score_team1 > score_team2:
    print(1)
else:
    print(2)
