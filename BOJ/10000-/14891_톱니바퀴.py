import sys

input = sys.stdin.readline


def rotate(arr, clockwise) -> list:
    if clockwise == 1:
        return [arr[-1]] + arr[:-1]
    else:
        return arr[1:] + [arr[0]]


def check_left(idx, clockwise) -> list:
    cur = 6
    target = 2
    rotated_gear = []

    for i in range(idx, 0, -1):
        if gear[i][cur] == gear[i - 1][target]:
            break

        clockwise *= -1
        rotated_gear.append((i - 1, clockwise))
        # cur, target = target, cur # 아 등신이네 이걸 왜 바꿔줬지;; 이거때매 틀림

    return rotated_gear


def check_right(idx, clockwise) -> list:
    cur = 2
    target = 6
    rotated_gear = []
    for i in range(idx, len(gear) - 1):
        if gear[i][cur] == gear[i + 1][target]:
            break

        clockwise *= -1
        rotated_gear.append((i + 1, clockwise))
        # cur, target = target, cur # 아 등신이네 이걸 왜 바꿔줬지;; 이거때매 틀림

    return rotated_gear


gear = []
for _ in range(4):
    gear.append(list(map(int, input().rstrip())))
K = int(input())  # 회전 수
for _ in range(K):
    gear_num, clockwise = map(int, input().split())
    rotated_gear = [(gear_num - 1, clockwise)]
    rotated_gear += check_left(gear_num - 1, clockwise) + check_right(gear_num - 1, clockwise)

    for gear_num, clockwise in rotated_gear:
        gear[gear_num] = rotate(gear[gear_num], clockwise)


ans = 0
score = 1
for i in range(4):
    if gear[i][0] == 1:
        ans += score
    score *= 2
print(ans)


"""
    14891. 톱니 바퀴
    - 문제에서 구현 하라는데로 하면 큰 문제 없이 할 수 있는듯
    - 다른 풀이를 보니 재귀로 구현한 사람이 많던데 나는 이번 회차에 돌아가는 톱니바퀴를 전부 구한뒤에 돌려주었다.
    - 체크해야 하는 톱니바퀴 번호가 바뀌는 걸로 착각해서 삽질함..
"""