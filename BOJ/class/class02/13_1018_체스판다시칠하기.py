

def check_board(board):
    # w_sieve = "WBWBWBWB"
    # b_sieve = "BWBWBWBW"

    # 1) W가 먼저인 체스판
    w_count = 0
    for i in range(8):
        for j in range(8):
            if (i+j) % 2 == 0:
                if board[i][j] != "W":
                    w_count += 1
            else:
                if board[i][j] != "B":
                    w_count += 1

    # 2) B가 먼저인 체스판
    b_count = 0
    for i in range(8):
        for j in range(8):
            if (i+j) % 2 == 0:
                if board[i][j] != "B":
                    b_count += 1
            else:
                if board[i][j] != "W":
                    b_count += 1

    return min(b_count, w_count)


n, m = map(int, input().split())
board = []

# board판 입력
for _ in range(n):
    board.append(input())

x = []
for i in range(n-7):
    for j in range(m-7):
        temp = [board[i+x][j:j+8] for x in range(8)]
        x.append(check_board(temp))

print(min(x))
