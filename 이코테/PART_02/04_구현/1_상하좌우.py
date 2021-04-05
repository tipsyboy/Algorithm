import sys


def solution1(n, plans):
    x, y = 1, 1
    for plan in plans:
        if plan == "U":
            if x < 2:
                continue
            x -= 1
        elif plan == "D":
            if x > n - 1:
                continue
            x += 1
        elif plan == "L":
            if y < 2:
                continue
            y -= 1
        elif plan == "R":
            if y > n - 1:
                continue
            y += 1

    print(x, y)


def solution2(n, plans):
    x, y = 1, 1
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    move_types = ["L", "R", "U", "D"]

    for plan in plans:
        for i in range(len(move_types)):
            if plan == move_types[i]:
                nx = x + dx[i]
                ny = y + dy[i]
                break

        if nx < 1 or nx > n or ny < 1 or ny > n:
            continue

        x, y = nx, ny

    print(x, y)


n = int(sys.stdin.readline())
plans = input().split()
solution1(n, plans)
solution2(n, plans)
