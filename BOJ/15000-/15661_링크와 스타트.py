# https://www.acmicpc.net/problem/15661

import sys
from itertools import combinations

input = sys.stdin.readline


def get_point(team: list) -> int:
    team_nums = len(team)
    point = 0
    for i in range(team_nums - 1):
        for j in range(i + 1, team_nums):
            point += synergy[team[i]][team[j]] + synergy[team[j]][team[i]]

    return point


N = int(input())
synergy = [list(map(int, input().split())) for _ in range(N)]
total = set(range(N))

ans = float("inf")
for i in range(1, N // 2 + 1):
    for c in combinations(range(N), i):
        start = get_point(list(c))
        link = get_point(list(total - set(c)))
        ans = min(ans, abs(start - link))
        if ans == 0:
            break
        # print(c, total - set(c), start, link, start - link, ans)
print(ans)


"""
15661. 링크와 스타트
    - 나올 수 있는 모든 팀조합을 combinations()으로 뽑아서 해결
    - 태그에 비트마스킹/백트래킹이 있는데 파이썬 combinations으로 개꿀로 해결가능

    - 미리 시너지를 합쳐 놓고 해결하는 방법이 있던데 뭔지 모르겠음.
"""