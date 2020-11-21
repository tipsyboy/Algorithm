# import time
import sys


# 3) 현재 노드의 가능 숫자 후보군을 찾고 넣는다.
def solve_sdoku(blank_num):
    if blank_num == len(blank_lst):  # 현재 빈칸 번호(노드번호)가 list의 길이와 같으면 종료
        for row in sdoku:
            print(" ".join(map(str, row)))
        sys.exit(0)

    # 현재 노드의 x, y좌표
    x = blank_lst[blank_num][0]  # 현재 노드(빈칸)의 x좌표
    y = blank_lst[blank_num][1]  # 현재 노드(빈칸)의 y좌표

    candidate = {1, 2, 3, 4, 5, 6, 7, 8, 9}  # 후보군
    sieve = set()

    # 스도쿠 판은 9x9판
    for i in range(9):
        # 가로 가능 숫자 후보군 탐색
        if sdoku[x][i]:
            sieve.add(sdoku[x][i])
            # 세로 가능 숫자 후보군 탐색
        if sdoku[i][y]:
            sieve.add(sdoku[i][y])

    # 현재 노드에 해당하는 3x3칸 확인하기
    x_3by3 = (x // 3) * 3
    y_3by3 = (y // 3) * 3

    for i in range(x_3by3, x_3by3 + 3):
        for j in range(y_3by3, y_3by3 + 3):
            if sdoku[i][j]:
                sieve.add(sdoku[i][j])

    candidate = candidate - sieve  # 후보군 탐색
    # 4) 현재 노드에 후보 숫자들을 차례로 넣는다.
    for candi in candidate:
        sdoku[x][y] = candi
        solve_sdoku(blank_num + 1)  # 다음 노드로 이동해서 탐색
        sdoku[x][y] = 0


# 1) 스도쿠판을 받아서
sdoku = [list(map(int, sys.stdin.readline().split())) for i in range(9)]
blank_lst = []  # 빈칸 좌표

# 2) sdoku판에서 빈칸(0)을 찾아내서 좌표 튜플을 저장한 리스트를 생성
for i in range(9):
    for j in range(9):
        if sdoku[i][j] == 0:
            blank_lst.append((i, j))


solve_sdoku(0)
