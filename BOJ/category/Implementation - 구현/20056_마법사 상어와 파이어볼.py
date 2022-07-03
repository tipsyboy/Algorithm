import sys
from collections import deque

input = sys.stdin.readline
directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


def move(N, graph) -> list:
    temp = [list(deque() for _ in range(N)) for __ in range(N)]

    for i in range(N):
        for j in range(N):
            for _ in range(len(graph[i][j])):
                fireball = graph[i][j].popleft()
                m, s, d = fireball[0], fireball[1], fireball[2]
                nr, nc = (i + directions[d][0] * s) % N, (j + directions[d][1] * s) % N

                temp[nr][nc].append((m, s, d))

    return temp


def choose_dir(q) -> bool:
    flag = 0 if q[0][2] % 2 == 0 else 1
    for i in range(len(q)):
        if q[i][2] % 2 == flag:
            continue
        return False

    return True


def sum_and_div(N, graph) -> list:
    temp = [list(deque() for _ in range(N)) for __ in range(N)]

    for i in range(N):
        for j in range(N):
            length = len(graph[i][j])
            if length == 0:
                continue

            if length == 1:
                temp[i][j].append(graph[i][j].popleft())
                continue

            sum_m = 0
            sum_s = 0
            new_dirs = [0, 2, 4, 6] if choose_dir(graph[i][j]) else [1, 3, 5, 7]
            for _ in range(len(graph[i][j])):
                fireball = graph[i][j].popleft()
                sum_m += fireball[0]
                sum_s += fireball[1]

            new_m = sum_m // 5
            new_s = sum_s // length
            if new_m == 0:
                continue

            for d in range(4):
                temp[i][j].append((new_m, new_s, new_dirs[d]))

    return temp


def cal_mass(N, graph) -> int:
    ans = 0
    for i in range(N):
        for j in range(N):
            for k in range(len(graph[i][j])):
                ans += graph[i][j][k][0]

    return ans


N, M, K = map(int, input().split())
graph = [list(deque() for _ in range(N)) for __ in range(N)]
for _ in range(M):
    r, c, m, s, d = map(int, input().split())  # 좌표, 질량, 속도, 방향
    graph[r - 1][c - 1].append((m, s, d))


for i in range(K):
    graph = move(N, graph)
    graph = sum_and_div(N, graph)

print(cal_mass(N, graph))


"""
20056. 마법사 상어와 파이어볼
    - 각 좌표에 deque을 정의해 구현
    - AC긴 한데 시간 복잡도가 마음에 들지 않아서, 다시 해볼 것 
"""