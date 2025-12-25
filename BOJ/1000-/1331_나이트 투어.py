# https://www.acmicpc.net/problem/1331

"""
1331. 나이트 투어
    1. 격자 만들기 - 꼭 그림처럼 만들지 않아도 동일한 의미를 가짐
    2. 명령 파싱
    3. 현재 위치에서 다음 위치로 갈 수 있는가? -> OOB, 방문, 갈 수 있는 점
    4. 마지막 명령 수행 후 시작 위치로 돌아 올 수 있나
"""


import sys

input = sys.stdin.readline
directions = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2)]


def parse_com(com: str) -> tuple:
    ny, nx = ord(com[0]) - 65, int(com[1]) - 1
    return (nx, ny)


def is_pos(x: int, y: int, nx: int, ny: int) -> bool:
    for d in range(8):
        tx, ty = x + directions[d][0], y + directions[d][1]

        if tx < 0 or tx >= 6 or ty < 0 or ty >= 6:
            continue
        if grid[tx][ty] == 1:
            continue
        if tx != nx or ty != ny:
            continue

        return True

    return False


grid = [[0] * 6 for _ in range(6)]
com = input().rstrip()
sx, sy = parse_com(com)
x, y = sx, sy

ans = "Valid"
for i in range(35):
    com = input().rstrip()
    nx, ny = parse_com(com)

    if not is_pos(x, y, nx, ny):
        ans = "Invalid"
        break

    grid[nx][ny] = 1
    x, y = nx, ny


if not is_pos(x, y, sx, sy):
    ans = "Invalid"

print(ans)