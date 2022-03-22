def solution(board, skill):
    row = len(board)
    col = len(board[0])
    dp = [[0] * (col + 1) for _ in range(row + 1)]

    for sk in skill:
        tp, r1, c1, r2, c2, degree = sk  # type, (r1, c1), (r2, c2), type의 정도
        if tp == 1:  # 적의 공격
            dp[r1][c1] -= degree
            dp[r1][c2 + 1] += degree
            dp[r2 + 1][c1] += degree
            dp[r2 + 1][c2 + 1] -= degree
        elif tp == 2:  # 아군의 회복 스킬
            dp[r1][c1] += degree
            dp[r1][c2 + 1] -= degree
            dp[r2 + 1][c1] -= degree
            dp[r2 + 1][c2 + 1] += degree

    # 누적 합
    for i in range(row):
        for j in range(1, col):
            dp[i][j] += dp[i][j - 1]

    for i in range(1, row):
        for j in range(col):
            dp[i][j] += dp[i - 1][j]

    # 남아있는 건물 세기
    cnt = 0
    for i in range(row):
        for j in range(col):
            if board[i][j] + dp[i][j] > 0:
                cnt += 1

    return cnt


# board = [[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]]
# skill = [[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]]
# print(solution(board, skill))

# board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# skill = [[1, 1, 1, 2, 2, 4], [1, 0, 0, 1, 1, 2], [2, 2, 0, 2, 0, 100]]
# print(solution(board, skill))


"""
    - 2차원 구간합을 생각하고 쿼리마다 dp테이블을 업데이트 하는 문제
      마지막에 dp테이블에 마킹 되어있는 쿼리들을 → ↓ 방향으로 누적 합 연산을 해주고
      board에 적용한 뒤 부셔지지 않은 건물 수를 세주면 된다. 
"""