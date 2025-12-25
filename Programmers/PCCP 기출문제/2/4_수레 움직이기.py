# https://school.programmers.co.kr/learn/courses/30/lessons/250134

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
R, C = -1, -1
RED, BLUE = "RED", "BLUE"
VISITED = {RED: [], BLUE: []}
RED_END, BLUE_END = tuple(), tuple()
INF = float("inf")
ANSWER = INF


def oob(x, y):
    return x < 0 or x >= R or y < 0 or y >= C


def is_cross(red, blue, red_nxt, blue_nxt):
    return red == blue_nxt and blue == red_nxt


def is_same_coord(rx, ry, bx, by):
    return rx == bx and ry == by


def init(maze):
    global R, C, VISITED, RED_END, BLUE_END

    R, C = len(maze), len(maze[0])
    VISITED[RED] = [[False] * C for _ in range(R)]
    VISITED[BLUE] = [[False] * C for _ in range(R)]

    red, blue = tuple(), tuple()
    for i in range(R):
        for j in range(C):
            if maze[i][j] == 1:
                red = (i, j)
                VISITED[RED][i][j] = True
            elif maze[i][j] == 2:
                blue = (i, j)
                VISITED[BLUE][i][j] = True
            elif maze[i][j] == 3:
                RED_END = (i, j)
            elif maze[i][j] == 4:
                BLUE_END = (i, j)
            elif maze[i][j] == 5:
                VISITED[RED][i][j] = True
                VISITED[BLUE][i][j] = True

    return red, blue


def get_nxt_list(cur, color):
    if color == RED and cur == RED_END or color == BLUE and cur == BLUE_END:
        return [cur]

    x, y = cur
    nxt_list = []
    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        if oob(nx, ny) or VISITED[color][nx][ny]:
            continue

        nxt_list.append((nx, ny))

    return nxt_list


def play(red_cur, blue_cur, cnt):
    global ANSWER

    if ANSWER < cnt:
        return

    if red_cur == RED_END and blue_cur == BLUE_END:
        ANSWER = min(ANSWER, cnt)
        return

    red_nxt = get_nxt_list(red_cur, RED)
    blue_nxt = get_nxt_list(blue_cur, BLUE)

    for rx, ry in red_nxt:
        for bx, by in blue_nxt:

            if is_same_coord(rx, ry, bx, by):
                continue
            if is_cross(red_cur, blue_cur, (rx, ry), (bx, by)):
                continue

            VISITED[RED][rx][ry] = True
            VISITED[BLUE][bx][by] = True
            play((rx, ry), (bx, by), cnt + 1)
            VISITED[RED][rx][ry] = False
            VISITED[BLUE][bx][by] = False


def solution(maze):
    red_cur, blue_cur = init(maze)
    play(red_cur, blue_cur, 0)

    return 0 if ANSWER == INF else ANSWER


# print(solution([[1, 4], [0, 0], [2, 3]]))
# print(solution([[1, 0, 2], [0, 0, 0], [5, 0, 5], [4, 0, 3]]))
# print(solution([[1, 5], [2, 5], [4, 5], [3, 5]]))
# print(solution([[4, 1, 2, 3]]))
