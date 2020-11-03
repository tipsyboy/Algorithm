
def repaint_CB(chess_board):
    sieve_b = ["B", "W", "B", "W", "B", "W", "B", "W"]
    sieve_w = ["W", "B", "W", "B", "W", "B", "W", "B"]

    # 체스판의 초항을 검은색으로 할 때,
    cnt_b = 0
    for i in range(8):
        for j in range(8):
            if i % 2 == 0:  # 체스판 짝수행
                if chess_board[i][j] != sieve_b[j]:  # 체랑 다르면
                    # chess_board[i][j] = check_b[j] # 바꿔줌 - 근데 수세는거라 굳이 바꾸지 않아도 됨
                    cnt_b += 1
            else:
                if chess_board[i][j] != sieve_w[j]:  # 체랑 다르면
                    # chess_board[i][j] = check_b[j] # 바꿔줌 - 근데 수세는거라 굳이 바꾸지 않아도 됨
                    cnt_b += 1

    # 체스판의 초항을 흰색으로 할 때,
    cnt_w = 0
    for i in range(8):
        for j in range(8):
            if i % 2 == 0:  # 체스판 짝수행
                if chess_board[i][j] != sieve_w[j]:  # 체랑 다르면
                    # chess_board[i][j] = check_b[j] # 바꿔줌 - 근데 수세는거라 굳이 바꾸지 않아도 됨
                    cnt_w += 1

            else:
                if chess_board[i][j] != sieve_b[j]:  # 체랑 다르면
                    # chess_board[i][j] = check_b[j] # 바꿔줌 - 근데 수세는거라 굳이 바꾸지 않아도 됨
                    cnt_w += 1

    return min(cnt_b, cnt_w)


height, width = map(int, input().split())  # 높이, 너비 받고
board = [list(input()) for i in range(height)]  # 보드 생성 - 2차원 배열
result_min = []  # 최솟값 배열

# (8*8) 정사각형 만들기 - (height-8+1)*(width-8+1) 개
for i in range(height-7):
    for j in range(width-7):
        chess_board = [board[i+k][j:j+8] for k in range(8)]  # (8*8) 체스보드 생성
        temp = repaint_CB(chess_board)  # 숫자세러 감
        result_min.append(temp)  # 받은 값을 추가

print(min(result_min))
