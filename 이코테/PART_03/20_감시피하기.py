import sys
from itertools import combinations

input = sys.stdin.readline

n = int(input())
graph = []
teachers = []
empty_space = []


def check(graph, teachers):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for teacher in teachers:
        x, y = teacher

        for i in range(4):
            for j in range(1, n):
                nx = x + dx[i] * j
                ny = y + dy[i] * j

                if nx < 0 or nx >= n or ny < 0 or ny >= n:  # 이 방향 볼때 맵 넘어가면
                    break
                if graph[nx][ny] == "O":  # 이 방향에 장애물 발견
                    break
                if graph[nx][ny] == "S":
                    return False

    return True


def set_obstacle(graph, empty_space, teachers):
    for obstacle_set in combinations(empty_space, 3):

        for x, y in obstacle_set:
            graph[x][y] = "O"

        if check(graph, teachers):
            return True

        for x, y in obstacle_set:
            graph[x][y] = "X"

    return False


for i in range(n):
    temp = list(map(str, input().split()))

    for j in range(n):
        if temp[j] == "X":
            empty_space.append((i, j))
        elif temp[j] == "T":
            teachers.append((i, j))

    graph.append(temp)

if set_obstacle(graph, empty_space, teachers):
    print("YES")
else:
    print("NO")


# 5
# X S X X T
# T X S X X
# X X X X X
# X T X X X
# X X T X X

# 4
# S S S T
# X X X X
# X X X X
# T T T X
