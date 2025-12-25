# https://www.acmicpc.net/problem/3126

"""
3126. 반역의 원철이
    - 모든 명령에 대해서 문제의 조건에 따라서 한번 명령을 변경하는 식으로 해결하면 TLE를 받는다.
      때문에 반복되는 명령수행에 대해서 효율적으로 접근해야 함.

    - 변경된 명령을 수행하기 이전에는 명령대로 움직이고 변경된 명령을 수행한 이후에는 일괄적으로 변경된 명령의 영향을 받는다. 
      이를 이용해서 주어진 명령에 대한 이동을 모두 기록한 후에 변경된 명령 이후에는 변경된 만큼 행동에 추가해 주면서 결과를 비교한다.

    - 이 코드가 정해인지는 모르겠으나, 질문 게시판에서도 같은 방향으로 푼사람이 있었음.

    - 너무 오래걸려서 어지러웠음
"""

import sys
from copy import deepcopy

input = sys.stdin.readline
directions = [(0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1)]


def dist_btw_points(x1: int, y1: int, x2: int, y2: int) -> float:
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def pos_init(x: int, y: int, d: int, command: list) -> list:
    pos = [(x, y)]
    for k in command:
        d = (d + k) % 8
        x, y = x + directions[d][0], y + directions[d][1]
        pos.append((x, y))

    return pos


def move(x: int, y: int, k: int, command: dict) -> tuple:
    for com in command.keys():
        x += directions[(com + k) % 8][0] * command[com]
        y += directions[(com + k) % 8][1] * command[com]

    return (x, y)


Xm, Ym, Xb, Yb = map(int, input().split())
N = int(input())
command = list(map(int, input().rstrip()))

pos = pos_init(Xm, Ym, 0, command)
psum = [0]
for i in range(N):
    psum.append((psum[-1] + command[i]) % 8)

cnt = [{psum[-1]: 1}]
for i in range(N - 1, 0, -1):
    new_dict = deepcopy(cnt[-1])
    new_dict[psum[i]] = new_dict.get(psum[i], 0) + 1
    cnt.append(new_dict)

ans = float("inf")
for i in range(1, N + 1):
    x, y = pos[i - 1][0], pos[i - 1][1]
    for j in range(8):
        nx, ny = move(x, y, (j - command[i - 1]), cnt[N - i])

        ans = min(ans, dist_btw_points(nx, ny, Xb, Yb))

print("%.6f" % ans)
