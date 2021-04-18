from itertools import combinations


# 학생 발견하기
def watch(x, y, direction):
    # 검사해서 S를 찾으면 True
    # 못찾으면 False를 리턴한다.

    if direction == 0:  # 상
        while True:
            if x < 0 or board[x][y] == "O":
                return False
            elif board[x][y] == "S":
                return True

            x -= 1
    elif direction == 1:  # 하
        while True:
            if x >= n or board[x][y] == "O":
                return False
            elif board[x][y] == "S":
                return True

            x += 1
    elif direction == 2:  # 좌
        while True:
            if y < 0 or board[x][y] == "O":
                return False
            elif board[x][y] == "S":
                return True

            y -= 1
    elif direction == 3:
        while True:
            if y >= n or board[x][y] == "O":
                return False
            elif board[x][y] == "S":
                return True

            y += 1


def check_map():
    for x, y in teachers:
        for direction in range(4):
            # 학생을 찾은 경우
            if watch(x, y, direction):
                return False

    return True


def solution():
    # 1. 벽을 3개 추가한 맵을 생성
    for candidate in combinations(empty, 3):
        for x, y in candidate:
            board[x][y] = "O"

        # 2. 1.에서 생성한 이번 맵 검사
        if check_map():  # 안 들키는 맵을 찾음
            return True

        for x, y in candidate:
            board[x][y] = "X"

    return False


n = int(input())
board = []
teachers = []
empty = []

for i in range(n):
    temp = list(input().split())

    for j in range(n):
        if temp[j] == "T":
            teachers.append((i, j))
        elif temp[j] == "X":
            empty.append((i, j))

    board.append(temp)

if solution():
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
