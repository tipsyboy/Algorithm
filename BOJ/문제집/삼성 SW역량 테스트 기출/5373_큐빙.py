import sys

input = sys.stdin.readline


def up():
    # up - 앞, 좌, 뒤, 우 의 0행 이동
    # cube[2][0]  # 앞
    # cube[4][0]  # 좌
    # cube[3][0]  # 뒤
    # cube[5][0]  # 우

    temp = cube[2][0]
    cube[2][0] = cube[5][0]
    cube[5][0] = cube[3][0]
    cube[3][0] = cube[4][0]
    cube[4][0] = temp
    self_rotate(0)  # 윗면 자체 돌리기


def down():
    # cube[2][2]  # 앞
    # cube[4][2]  # 좌
    # cube[3][2]  # 뒤
    # cube[5][2]  # 우
    temp = cube[2][2]
    cube[2][2] = cube[4][2]
    cube[4][2] = cube[3][2]
    cube[3][2] = cube[5][2]
    cube[5][2] = temp
    self_rotate(1)


def front():
    # 앞면 시계방향 - 윗면2행, 우측면 0열, 아랫면 0행, 좌측면 2열
    cube[0][2][0], cube[0][2][1], cube[0][2][2]  # 윗
    cube[5][0][0], cube[5][1][0], cube[5][2][0]  # 우
    cube[1][0][0], cube[1][0][1], cube[1][0][2]  # 아
    cube[4][0][2], cube[4][1][2], cube[4][2][2]  # 좌

    temp0, temp1, temp2 = cube[0][2][0], cube[0][2][1], cube[0][2][2]
    cube[0][2][0], cube[0][2][1], cube[0][2][2] = cube[4][2][2], cube[4][1][2], cube[4][0][2]
    cube[4][0][2], cube[4][1][2], cube[4][2][2] = cube[1][0][0], cube[1][0][1], cube[1][0][2]
    cube[1][0][0], cube[1][0][1], cube[1][0][2] = cube[5][2][0], cube[5][1][0], cube[5][0][0]
    cube[5][0][0], cube[5][1][0], cube[5][2][0] = temp0, temp1, temp2
    self_rotate(2)


def back():
    # 뒷면 시계 - 윗0행, 좌0열, 아래 2행, 우측2열
    cube[0][0][0], cube[0][0][1], cube[0][0][2]  # 윗
    cube[4][0][0], cube[4][1][0], cube[4][2][0]  # 좌
    cube[1][2][0], cube[1][2][1], cube[1][2][2]  # 아래
    cube[5][0][2], cube[5][1][2], cube[5][2][2]  # 우측

    temp0, temp1, temp2 = cube[0][0][0], cube[0][0][1], cube[0][0][2]
    cube[0][0][0], cube[0][0][1], cube[0][0][2] = cube[5][0][2], cube[5][1][2], cube[5][2][2]
    cube[5][0][2], cube[5][1][2], cube[5][2][2] = cube[1][2][2], cube[1][2][1], cube[1][2][0]
    cube[1][2][0], cube[1][2][1], cube[1][2][2] = cube[4][0][0], cube[4][1][0], cube[4][2][0]
    cube[4][0][0], cube[4][1][0], cube[4][2][0] = temp2, temp1, temp0
    self_rotate(3)


def left():
    # 좌측 시계 - 위0열, 앞0열, 밑0열, 뒤 2열 -> 뒷면주의
    # 돌때 뒤집어서 들어가는거 주의 (2면)
    cube[0][0][0], cube[0][1][0], cube[0][2][0]  # 위
    cube[2][0][0], cube[2][1][0], cube[2][2][0]  # 앞
    cube[1][0][0], cube[1][1][0], cube[1][2][0]  # 밑
    cube[3][0][2], cube[3][1][2], cube[3][2][2]  # 뒤

    temp0, temp1, temp2 = cube[0][0][0], cube[0][1][0], cube[0][2][0]
    cube[0][0][0], cube[0][1][0], cube[0][2][0] = cube[3][2][2], cube[3][1][2], cube[3][0][2]
    cube[3][0][2], cube[3][1][2], cube[3][2][2] = cube[1][2][0], cube[1][1][0], cube[1][0][0]
    cube[1][0][0], cube[1][1][0], cube[1][2][0] = cube[2][0][0], cube[2][1][0], cube[2][2][0]
    cube[2][0][0], cube[2][1][0], cube[2][2][0] = temp0, temp1, temp2
    self_rotate(4)


def right():
    # 우측 시계 - 위 2열, 뒤 0열, 아래 2열, 앞 2열
    cube[0][0][2], cube[0][1][2], cube[0][2][2]  # 위
    cube[3][0][0], cube[3][1][0], cube[3][2][0]  # 뒤
    cube[1][0][2], cube[1][1][2], cube[1][2][2]  # 아래
    cube[2][0][2], cube[2][1][2], cube[2][2][2]  # 앞

    temp0, temp1, temp2 = cube[0][0][2], cube[0][1][2], cube[0][2][2]
    cube[0][0][2], cube[0][1][2], cube[0][2][2] = cube[2][0][2], cube[2][1][2], cube[2][2][2]
    cube[2][0][2], cube[2][1][2], cube[2][2][2] = cube[1][0][2], cube[1][1][2], cube[1][2][2]
    cube[1][0][2], cube[1][1][2], cube[1][2][2] = cube[3][2][0], cube[3][1][0], cube[3][0][0]
    cube[3][0][0], cube[3][1][0], cube[3][2][0] = temp2, temp1, temp0
    self_rotate(5)


def self_rotate(p):
    # 겉 껍질
    temp = cube[p][0][0]
    cube[p][0][0] = cube[p][2][0]
    cube[p][2][0] = cube[p][2][2]
    cube[p][2][2] = cube[p][0][2]
    cube[p][0][2] = temp

    # 속
    temp = cube[p][0][1]
    cube[p][0][1] = cube[p][1][0]
    cube[p][1][0] = cube[p][2][1]
    cube[p][2][1] = cube[p][1][2]
    cube[p][1][2] = temp


# 큐브
# U상 D하 F앞 B뒤 L좌 R우
def simulation(plane, count):
    if plane == "U":
        for _ in range(count):
            up()
    elif plane == "D":
        for _ in range(count):
            down()
    elif plane == "F":
        for _ in range(count):
            front()
    elif plane == "B":
        for _ in range(count):
            back()
    elif plane == "L":
        for _ in range(count):
            left()
    elif plane == "R":
        for _ in range(count):
            right()


TC = int(input())
for _ in range(TC):
    cube = [
        [["w", "w", "w"], ["w", "w", "w"], ["w", "w", "w"]],  # 위
        [["y", "y", "y"], ["y", "y", "y"], ["y", "y", "y"]],  # 아래
        [["r", "r", "r"], ["r", "r", "r"], ["r", "r", "r"]],  # 앞
        [["o", "o", "o"], ["o", "o", "o"], ["o", "o", "o"]],  # 뒤
        [["g", "g", "g"], ["g", "g", "g"], ["g", "g", "g"]],  # 좌
        [["b", "b", "b"], ["b", "b", "b"], ["b", "b", "b"]],  # 우
    ]

    n = int(input())
    command = input().split()
    for plane, clockwise in command:
        # print(plane, clockwise)
        count = 1 if clockwise == "+" else 3
        simulation(plane, count)
    for i in range(3):
        print("".join(cube[0][i]))

# cube = [
#     [["w", "w", "w"], ["w", "w", "w"], ["w", "w", "w"]],  # 위
#     [["y", "y", "y"], ["y", "y", "y"], ["y", "y", "y"]],  # 아래
#     [["r", "r", "r"], ["r", "r", "r"], ["r", "r", "r"]],  # 앞
#     [["o", "o", "o"], ["o", "o", "o"], ["o", "o", "o"]],  # 뒤
#     [["g", "g", "g"], ["g", "g", "g"], ["g", "g", "g"]],  # 좌
#     [["b", "b", "b"], ["b", "b", "b"], ["b", "b", "b"]],  # 우
# ]

# up()
# right()
# right()
# front()
# front()
# right()
# right()
# up()
# front()
# front()
# right()
# for i in range(6):
#     print(*cube[i], sep="\n")
#     print()

"""
               [0]
               WWW            
               WWW
               WWW
          [4]  [2]  [5]  [3]
          GGG  RRR  BBB  OOO
          GGG  RRR  BBB  OOO
          GGG  RRR  BBB  OOO
               [1]
               YYY
               YYY
               YYY  
"""

"""
    5373. 큐빙
    
    - 하...

"""