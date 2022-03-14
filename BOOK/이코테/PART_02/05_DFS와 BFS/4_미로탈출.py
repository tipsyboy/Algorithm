from collections import deque


def maze_bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()

        # 상하좌우 방향 만들어 주기
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if maze[nx][ny] == 0:
                continue

            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))


n, m = map(int, input().split())

# 상하좌우 x, y의 변화 값
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

maze = []
for i in range(n):
    maze.append(list(map(int, input())))

maze_bfs(0, 0)
print(maze)
print(maze[n - 1][m - 1])


# test case
# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111
