# 2024.10.10 THU
# https://www.acmicpc.net/problem/17143

import sys

input = sys.stdin.readline


# 2. 상어 잡이
def catch_shark(y):
    for i in range(1, R + 1):
        if (i, y) in shark:
            return shark.pop((i, y))[2]

    return 0


# 3. 상어의 이동
def move_sharks():
    moved_shark = dict()

    for pos in shark.keys():
        s, d, z = shark[pos]
        x, y = pos
        action = s % (2 * (R - 1)) if d in (1, 2) else s % (2 * (C - 1))

        while action:
            if d == 1:
                t = max(x - action, 1)
                move = x - t
                x = t
                action -= move
                if action:
                    d = 2
            elif d == 2:
                t = min(x + action, R)
                move = t - x
                x = t
                action -= move
                if action:
                    d = 1
            elif d == 3:
                t = min(y + action, C)
                move = t - y
                y = t
                action -= move
                if action:
                    d = 4
            elif d == 4:
                t = max(y - action, 1)
                move = y - t
                y = t
                action -= move
                if action:
                    d = 3

        if (x, y) not in moved_shark:
            moved_shark[(x, y)] = []
        moved_shark[(x, y)].append((s, d, z))

    return moved_shark


# 4. 겹친 상어를 정리한다.
def remove_sharks(moved_shark):
    new_shark = dict()
    for pos, sharks in moved_shark.items():
        new_shark[pos] = max(sharks, key=lambda x: x[2])

    return new_shark


R, C, M = map(int, input().split())
fisherman = []
shark = dict()
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    shark[(r, c)] = (s, d, z)

ans = 0
for y in range(1, C + 1):  # 1. 낚시왕의 이동
    # 2. 상어 잡이
    ans += catch_shark(y)
    # 3. 상어의 이동
    moved_shark = move_sharks()
    # 4. 겹친 상어를 정리한다.
    shark = remove_sharks(moved_shark)

print(ans)
