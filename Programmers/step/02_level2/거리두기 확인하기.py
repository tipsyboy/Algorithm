from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def checking(place, sy, sx):
    q = deque([(sy, sx)])
    visited = [[False] * 5 for _ in range(5)]
    visited[sy][sx] = True
    idx = 2
    while q and idx:
        y, x = q.popleft()

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]

            if 0 <= ny < 5 and 0 <= nx < 5 and not visited[ny][nx]:
                if place[ny][nx] == "P":
                    return False

                if place[ny][nx] == "O":
                    q.append((ny, nx))
                    visited[ny][nx] = True
        idx -= 1

    return True


def find_p(place):
    for i in range(5):
        for j in range(5):
            if place[i][j] == "P" and not checking(place, i, j):
                return 0

    return 1


def solution(places):
    rst = [0] * 5
    for i, place in enumerate(places):
        rst[i] = find_p(place)

    return rst


places = [
    ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
    ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
    ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
    ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
    ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"],
]

print(solution(places))
