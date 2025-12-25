import sys
from itertools import combinations

input = sys.stdin.readline
INF = int(1e9)


def get_score(combi):
    global rst

    team1_score = 0
    team2_score = 0
    team1 = []
    team2 = []

    for i in range(n):
        if i in combi:
            team1.append(i)
        else:
            team2.append(i)

    if tuple(team1) not in team_matching:
        team_matching.add(tuple(team1))
        team_matching.add(tuple(team2))

        for i, j in combinations(team1, 2):
            team1_score += graph[i][j] + graph[j][i]
        for i, j in combinations(team2, 2):
            team2_score += graph[i][j] + graph[j][i]

        rst = min(abs(team2_score - team1_score), rst)


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
team_matching = set()

rst = INF

for combi in combinations(range(n), n // 2):
    get_score(combi)

print(rst)
