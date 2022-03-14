import sys

input = sys.stdin.readline


n, m = map(int, input().split())
x, y, direction = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

graph[x][y] = 1
count = 1
visited = [[False] * m for _ in range(n)]  # 방문배열

while True:
    move = False

    for _ in range(4):
        if direction == 0:
            direction = 3
        else:
            direction -= 1

        nx = x + dx[direction]
        ny = y + dy[direction]

        if 0 <= nx < n and 0 <= ny < n:
            if not visited[nx][ny] and graph[nx][ny] != 1:
                x, y = nx, ny
                visited[nx][ny] = True
                count += 1
                move = True
                break

    # 이동 불가인 경우 - 뒤에 바다만 없다면 이동한다.(방문했어도)
    if not move:
        nx = x - dx[direction]
        ny = y - dy[direction]

        if graph[nx][ny] != 1:
            x, y = nx, ny
        else:
            break

print(count)


"""
PART2 구현. 게임 개발 

    - 이동 불가인 경우 뒤로 가는 경우에서 헷갈렸다.
      이미 이동불가인 경우는 뒤로도 못간다고 생각했는데,
      단순히 캐릭터가 방문할 수 있는 최대 수만 세는거라 이미 방문한 곳이라도 뒤에 바다만 없으면 뒤로 이동해서 재탐색한다. 

      대신에 위처럼 이동한 경우 이미 탐색한 공간이기 때문에 count는 하지 않는다. 
"""