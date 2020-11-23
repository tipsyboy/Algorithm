import sys


def promising(x, y, candidate):
    # 현재 노드의 가로 check
    if candidate in sudoku[x]:
        return False
    for i in range(9):
        # # 현재 노드의 가로 check
        # if sudoku[x][i] == candidate:
        #     return False
        # 현재 노드의 세로 check
        if sudoku[i][y] == candidate:
            return False

    # 현재 노드의 3x3칸 check
    x_3by3 = (x // 3) * 3
    y_3by3 = (y // 3) * 3
    for i in range(x_3by3, x_3by3+3):
        for j in range(y_3by3, y_3by3+3):
            if sudoku[i][j] == candidate:
                return False

    return True


def solve_sudoku(blank_num):
    # 더이상 찾을 노드가 없는 경우에
    if blank_num == len(blank_lst):
        for row in sudoku:
            print(" ".join(map(str, row)))
        sys.exit(0)  # 여러개여도 하나만 출력할 것임
    # 스도쿠판의 빈칸(현재 노드)으로 들어와서 ex)blank_num == 0 -> 0번째 노드
    x = blank_lst[blank_num][0]  # 튜플 0번째 값 == x좌표
    y = blank_lst[blank_num][1]  # 튜플 1번째 값 == y좌표

    # 노드에 들어갈 수 있는 숫자 후보 1~9
    for candidate in range(1, 10):
        if promising(x, y, candidate):  # 유망한가?
            sudoku[x][y] = candidate  # 유망하면 현재 좌표에 후보값을 넣고
            solve_sudoku(blank_num+1)  # 다음 노드로 재탐색
            sudoku[x][y] = 0  # 값이 아니었다면 돌아와서 0넣음


# 1) 스도쿠판을 받아서
sudoku = [list(map(int, sys.stdin.readline().split())) for i in range(9)]
blank_lst = []  # 빈칸 좌표

# 2) sdoku판에서 빈칸(0)을 찾아내서 좌표 튜플을 저장한 리스트를 생성
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            blank_lst.append((i, j))

solve_sudoku(0)  # 호출
