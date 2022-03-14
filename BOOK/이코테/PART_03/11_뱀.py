import sys
from collections import deque

input = sys.stdin.readline


# 뱀의 방향 (동, 남, 서, 북 순서) 90도씩 이동하기 위해
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# init input data
n = int(input())  # map 크기
graph = [[0] * n for _ in range(n)]  # map

apple = int(input())  # 사과 수
for _ in range(apple):
    row, col = map(int, input().split())  # 사과의 좌표

    graph[row - 1][col - 1] = 9  # 사과를 9로 표시

m = int(input())  # 방향 변환 정보 수
command = deque()
for _ in range(m):
    x, c = map(str, input().split())
    command.append((int(x), c))


def turn_direction(direction, com):
    if com == "L":
        return (direction - 1) % 4
    elif com == "D":
        return (direction + 1) % 4


def simulation(command, sx, sy, direction):
    time = 0  # 지나간 시간
    graph[sx][sy] = 1  # 뱀은 1로 표시
    snake = deque()  # *** 뱀이 있는 좌표들 - deque()이므로 0번 data가 꼬리의 좌표가 된다.
    snake.append((sx, sy))  #

    # simulation
    while True:
        # 방향 이동 - 방향 정보가 남아있고, command가 time 과 일치하는 경우
        if command and command[0][0] == time:
            direction = turn_direction(direction, command.popleft()[1])

        # 다음 머리 좌표
        nx = sx + dx[direction]
        ny = sy + dy[direction]

        # 게임이 끝나는 경우
        if nx < 0 or nx >= n or ny < 0 or ny >= n or graph[nx][ny] == 1:
            return time + 1  # 부딪치기까지 time을 쓰므로 + 1

        # 사과가 없다. - 꼬리 당겨오기
        if graph[nx][ny] != 9:
            x, y = snake.popleft()
            graph[x][y] = 0

        #
        graph[nx][ny] = 1  # 머리 이동
        snake.append((nx, ny))  # 뱀에 늘어난 길이 추가
        sx, sy = nx, ny  # 머리 좌표 변경
        time += 1  # 시간 증가


print(simulation(command, 0, 0, 0))


"""
11. 뱀 boj 3190.
    - 문제의 조건이 아주 친절하게 나와 있어서 그대로 진행하면 되지만, 
      뱀이 사과를 먹지 않았을때, 꼬리를 당겨오는 부분을 잠시 생각해야한다.

      처음에는 꼬리의 좌표 값을 따로 저장해서 graph에서 꼬리 좌표 값을 0으로 바꿔주는 방식을 생각했으나, 
      이렇게 하면 다음 꼬리가 되는 좌표를 지정할 수 가 없다 (연결되있지 않다!)
      따라서 뱀을 연결리스트의 종류로 표현해야 하는데, 뱀의 꼬리의 경우 가장 먼저 들어온 값으로 
      가장 먼저 나가야한다. 따라서 큐를 사용해서 뱀을 표현하고 사과를 먹으므로써 늘어난 뱀의 머리를 큐에 집어 넣고
      사과를 먹지 못했을때, 당겨오는 꼬리의 좌표를 큐로 빼내면 된다.

    - 시간 값 리턴 부분에서 time + 1을 리턴하는 이유는 부딪치기 까지도 시간을 소비하기 때문이다. 

    - python의 경우 -1 % 4의 값은 3이다. 따라서 방향을 L로 바꿀때 현재 방향이 0인 경우
      조건 분기를 통하지 않고 그냥 계산해도 값이 잘 나온다. 
"""


# test case
# 6
# 3
# 3 4
# 2 5
# 5 3
# 3
# 3 D
# 15 L
# 17 D

# 10
# 4
# 1 2
# 1 3
# 1 4
# 1 5
# 4
# 8 D
# 10 D
# 11 D
# 13 L


# 10
# 5
# 1 5
# 1 3
# 1 2
# 1 6
# 1 7
# 4
# 8 D
# 10 D
# 11 D
# 13 L
