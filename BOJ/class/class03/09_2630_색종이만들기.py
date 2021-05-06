n = int(input())
board = []

for _ in range(n):
    board.append(list(map(int, input().split())))


def check_board(x, y, length):  # 종이 시작점의 x, y좌표, 길이
    flag = board[x][y]

    for i in range(x, x + length):
        for j in range(y, y + length):
            if board[i][j] != flag:
                return False

    return True


def cut_board(x, y, length):
    global blue, white

    if check_board(x, y, length):
        if board[x][y] == 1:
            blue += 1
        else:
            white += 1
    else:
        cut_board(x, y, length//2)  # 1사분면
        cut_board(x, y+length//2, length//2)  # 2
        cut_board(x + length//2, y, length//2)  # 3
        cut_board(x+length//2, y+length//2, length//2)  # 4


blue, white = 0, 0
cut_board(0, 0, n)

print(white)
print(blue)
