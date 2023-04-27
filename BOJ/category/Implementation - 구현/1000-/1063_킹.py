# https://www.acmicpc.net/problem/1063

import sys

input = sys.stdin.readline
directions = {
    "R": (0, 1),
    "L": (0, -1),
    "B": (1, 0),
    "T": (-1, 0),
    "RT": (-1, 1),
    "LT": (-1, -1),
    "RB": (1, 1),
    "LB": (1, -1),
}


def OOB(x: int, y: int) -> bool:
    return True if x < 0 or x >= 8 or y < 0 or y >= 8 else False


k, s, N = input().split()
king = (8 - int(k[1]), ord(k[0]) - 65)
stone = (8 - int(s[1]), ord(s[0]) - 65)

for _ in range(int(N)):
    com = input().rstrip()

    nx, ny = king[0] + directions[com][0], king[1] + directions[com][1]

    if OOB(nx, ny):
        continue

    # move stone
    if (nx, ny) == stone:
        snx, sny = stone[0] + directions[com][0], stone[1] + directions[com][1]

        if OOB(snx, sny):
            continue

        stone = (snx, sny)

    king = (nx, ny)


print(chr(king[1] + 65) + str(8 - king[0]))
print(chr(stone[1] + 65) + str(8 - stone[0]))

"""
1063. 킹
    - 그냥 구현
"""