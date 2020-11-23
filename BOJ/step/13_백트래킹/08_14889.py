# 1이 있는팀 vs 없는팀 구성 -> 중복 제거

import sys


def check_team_stat(team_A):
    team_A_rst = 0  # 점수
    team_B_rst = 0

    team_B = sieve - team_A

    for i in team_A:
        for j in team_A:
            if i == j:
                continue

            team_A_rst += score_board[i][j]

    for i in team_B:
        for j in team_B:
            if i == j:
                continue

            team_B_rst += score_board[i][j]

    team_stat.append(abs(team_A_rst-team_B_rst))


def make_team(level):
    # 한 팀을 다 정한 경우.
    if level == n//2:
        team.add(n-1)
        check_team_stat(team)
        team.discard(n-1)
        return

    for i in range(n-1):
        if check_promising[i]:
            team.add(i)
            check_promising[i] = False
            make_team(level+1)
            team.remove(i)

            for j in range(i+1, n-1):
                check_promising[j] = True


n = int(sys.stdin.readline())
check_promising = [True] * (n-1)
score_board = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
team = set()  # 한 팀
team_stat = []  # 팀이 될 수 있는 경우의 수.
sieve = set(i for i in range(n))  # (n-1)이 없는 팀 걸러내기

make_team(1)
print(min(team_stat))
