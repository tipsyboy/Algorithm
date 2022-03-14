# 팀의 이름은 root가 팀의 이름이 된다~
def find_team(parent, x):
    if parent[x] != x:
        parent[x] = find_team(parent, parent[x])

    return parent[x]


# 팀 합치기
def union_team(parent, x, y):
    x = find_team(parent, x)
    y = find_team(parent, y)

    if x < y:
        team[y] = x
    else:
        team[x] = y


n, m = map(int, input().split())
team = [0] * (n + 1)

for i in range(n+1):
    team[i] = i


for _ in range(m):
    command, a, b = map(int, input().split())

    if command == 0:
        union_team(team, a, b)
    elif command == 1:
        if find_team(team, a) == find_team(team, b):
            print("YES")
        else:
            print("NO")


# # test case
# 7 8
# 0 1 3
# 1 1 7
# 0 7 6
# 1 7 1
# 0 3 7
# 0 4 2
# 0 1 1
# 1 1 1
