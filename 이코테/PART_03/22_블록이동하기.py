import sys
from collections import deque


def solution(board):
    # direction - 상 하 좌 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    n = len(board)  # map size
    q = deque()
    visited = []
    q.append({(0, 0), (0, 1)})  # 시작점
    visited.append({(0, 0), (0, 1)})
    time = 0

    while q:
        length = len(q)

        for _ in range(length):
            pos = q.popleft()

            if (n - 1, n - 1) in pos:
                return time

            pos = list(pos)
            x1, y1, x2, y2 = pos[0][0], pos[0][1], pos[1][0], pos[1][1]

            # 1. 상하좌우 이동
            for i in range(4):
                nx1, nx2 = x1 + dx[i], x2 + dx[i]
                ny1, ny2 = y1 + dy[i], y2 + dy[i]

                if 0 <= nx1 < n and 0 <= ny1 < n and 0 <= nx2 < n and 0 <= ny2 < n:
                    if board[nx1][ny1] != 1 and board[nx2][ny2] != 1:
                        if {(nx1, ny1), (nx2, ny2)} not in visited:
                            q.append({(nx1, ny1), (nx2, ny2)})
                            visited.append({(nx1, ny1), (nx2, ny2)})

            # 2. 회전 이동
            if x1 == x2:  # 행 좌표가 같은 경우 - 가로로 놓임
                for i in [-1, 1]:
                    nx = x1 + i

                    if 0 <= nx < n and board[nx][y1] != 1 and board[nx][y2] != 1:
                        if {(x1, y1), (nx, y1)} not in visited:
                            q.append({(x1, y1), (nx, y1)})
                            visited.append({(x1, y1), (nx, y1)})
                        if {(x2, y2), (nx, y2)} not in visited:
                            q.append({(x2, y2), (nx, y2)})
                            visited.append({(x2, y2), (nx, y2)})
            elif y1 == y2:  # 열 좌표가 같은 경우 - 세로로 놓임
                for i in [-1, 1]:
                    ny = y1 + i

                    if 0 <= ny < n and board[x1][ny] != 1 and board[x2][ny] != 1:
                        if {(x1, y1), (x1, ny)} not in visited:
                            q.append({(x1, y1), (x1, ny)})
                            visited.append({(x1, y1), (x1, ny)})
                        if {(x2, y2), (x2, ny)} not in visited:
                            q.append({(x2, y2), (x2, ny)})
                            visited.append({(x2, y2), (x2, ny)})

        time += 1


print(
    solution(
        [
            [0, 0, 0, 1, 1],
            [0, 0, 0, 1, 0],
            [0, 1, 0, 1, 1],
            [1, 1, 0, 0, 1],
            [0, 0, 0, 0, 0],
        ]
    )
)


####

# def get_next_positions(pos, board):
#     n = len(board)
#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]

#     pos = list(pos)
#     x1, y1, x2, y2 = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
#     next_positions = []

#     # 1. 상하좌우 이동
#     for i in range(4):
#         nx1, nx2 = x1 + dx[i], x2 + dx[i]
#         ny1, ny2 = y1 + dy[i], y2 + dy[i]

#         if 0 <= nx1 < n and 0 <= ny1 < n and 0 < nx2 < n and 0 <= ny2 < n:
#             if board[nx1][ny1] != 1 and board[nx2][ny2] != 1:
#                 next_positions.append({(nx1, ny1), (nx2, ny2)})

#     # 2. 회전 이동
#     if x1 == x2:  # 행 값이 같은 경우 - 가로로 놓여진 경우
#         for i in [-1, 1]:
#             nx = x1 + i

#             if 0 <= nx < n and board[nx][y1] != 1 and board[nx][y2] != 1:
#                 next_positions.append({(x1, y1), (nx, y1)})
#                 next_positions.append({(x2, y2), (nx, y2)})

#     elif y1 == y2:  # 열 값이 같은 경우 - 세로로 놓여진 경우
#         for i in [-1, 1]:
#             ny = y1 + i

#             if 0 <= ny < n and board[x1][ny] != 1 and board[x2][ny] != 1:
#                 next_positions.append({(x1, y1), (x1, ny)})
#                 next_positions.append({(x2, y2), (x2, ny)})

#     return next_positions