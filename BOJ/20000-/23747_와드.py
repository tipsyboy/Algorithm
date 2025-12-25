import sys
from collections import deque

input = sys.stdin.readline
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(sx, sy, alpha) -> None:
    q = deque([(sx, sy)])
    ans[sx][sy] = "."

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + directions[i][0], y + directions[i][1]

            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                continue
            if ans[nx][ny] == "." or graph[nx][ny] != alpha:
                continue

            q.append((nx, ny))
            ans[nx][ny] = "."


R, C = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(R)]
sx, sy = map(lambda x: int(x) - 1, input().split())  # start
command = input().rstrip()

wards = []
hx, hy = sx, sy
for com in command:
    if com == "W":
        wards.append((hx, hy))
    elif com == "U":
        hx -= 1
    elif com == "D":
        hx += 1
    elif com == "L":
        hy -= 1
    elif com == "R":
        hy += 1

ans = [["#"] * C for _ in range(R)]
for x, y in wards:
    if ans[x][y] == ".":
        continue
    bfs(x, y, graph[x][y])

ans[hx][hy] = "."
for i in range(4):
    nx, ny = hx + directions[i][0], hy + directions[i][1]
    if nx < 0 or nx >= R or ny < 0 or ny >= C:
        continue
    ans[nx][ny] = "."

# print
for i in range(R):
    print("".join(ans[i]))


"""
23747. 와드 
    - 단순 bfs
"""