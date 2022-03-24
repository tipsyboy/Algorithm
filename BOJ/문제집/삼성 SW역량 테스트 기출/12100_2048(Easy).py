import sys
from copy import deepcopy

input = sys.stdin.readline
ANSWER = -1


def get_next_position(x, y, direction, board) -> list:
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우

    while True:
        nx, ny = x + directions[direction][0], y + directions[direction][1]

        if nx < 0 or nx >= N or ny < 0 or ny >= N or board[nx][ny]:
            break

        x, y = nx, ny

    cx, cy = x, y
    if 0 <= x + directions[direction][0] < N and 0 <= y + directions[direction][1] < N:
        cx, cy = x + directions[direction][0], y + directions[direction][1]

    return [x, y, cx, cy]  # (x, y):다음 갈 위치 (cx, cy): 합쳐질 수도 있는 위치


def move_up(N, board) -> list:
    sumed_pos = set()  # 이미 합쳐진 위치의 좌표

    for i in range(1, N):
        for j in range(N):
            if board[i][j] == 0:
                continue

            x, y, cx, cy = get_next_position(i, j, 0, board)
            if board[cx][cy] == board[i][j] and (cx, cy) not in sumed_pos:
                board[cx][cy] += board[i][j]
                board[i][j] = 0
                sumed_pos.add((cx, cy))
            else:
                board[x][y], board[i][j] = board[i][j], board[x][y]

    return board


def move_down(N, board) -> list:
    sumed_pos = set()

    for i in range(N - 2, -1, -1):
        for j in range(N):
            if board[i][j] == 0:
                continue

            x, y, cx, cy = get_next_position(i, j, 1, board)
            if board[cx][cy] == board[i][j] and (cx, cy) not in sumed_pos:
                board[cx][cy] += board[i][j]
                board[i][j] = 0
                sumed_pos.add((cx, cy))
            else:
                board[x][y], board[i][j] = board[i][j], board[x][y]

    return board


def move_left(N, board) -> list:
    sumed_pos = set()

    for i in range(1, N):  # 열
        for j in range(N):  # 행
            if board[j][i] == 0:
                continue

            x, y, cx, cy = get_next_position(j, i, 2, board)
            if board[cx][cy] == board[j][i] and (cx, cy) not in sumed_pos:
                board[cx][cy] += board[j][i]
                board[j][i] = 0
                sumed_pos.add((cx, cy))
            else:
                board[x][y], board[j][i] = board[j][i], board[x][y]

    return board


def move_right(N, board) -> list:
    sumed_pos = set()

    for i in range(N - 2, -1, -1):  # 열
        for j in range(N):  # 행
            if board[j][i] == 0:
                continue

            x, y, cx, cy = get_next_position(j, i, 3, board)
            if board[cx][cy] == board[j][i] and (cx, cy) not in sumed_pos:
                board[cx][cy] += board[j][i]
                board[j][i] = 0
                sumed_pos.add((cx, cy))
            else:
                board[x][y], board[j][i] = board[j][i], board[x][y]

    return board


def check_num(board) -> int:
    max_val = -1
    for i in range(N):
        for j in range(N):
            if max_val < board[i][j]:
                max_val = board[i][j]

    return max_val


def copy_map(N, board) -> list:
    temp = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            temp[i][j] = board[i][j]

    return temp


def DFS(depth, board) -> None:
    global ANSWER

    if depth == 5:
        ANSWER = max(ANSWER, check_num(board))
        return

    copy_board = copy_map(N, board)
    # copy_board = deepcopy(board) # 딥카피가 확실히 느리네;;
    DFS(depth + 1, move_up(N, copy_board))
    copy_board = copy_map(N, board)
    DFS(depth + 1, move_down(N, copy_board))
    copy_board = copy_map(N, board)
    DFS(depth + 1, move_left(N, copy_board))
    copy_board = copy_map(N, board)
    DFS(depth + 1, move_right(N, copy_board))


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

DFS(0, board)
print(ANSWER)


"""
    12100. 2048 (Easy)
    - 삼성 기출답게 빡구현 문제
    
    - 각 move에 따라 함수를 따로 정의하고 5번째에 가장 큰 블록을 세주는 단순 로직
      but, 배열을 매개변수로 사용할때, 콜방식에 대해서 착각해서 오랫동안 삽질해서 풀었다..
      사람이 아프면 확실히 제정신은 아닌듯
"""