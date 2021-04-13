n = int(input())  # n * n 맵
k = int(input())  # 사과 개수

data = [[0] * n for _ in range(n)]  # 맵 정보
change_direction = []

# 사과 정보 입력 받기
for _ in range(k):
    x, y = map(int, input().split())
    data[x - 1][y - 1] = 1

# 회전 정보를 입력 받는다.
cd = int(input())
for _ in range(cd):
    sec, d = input().split()
    change_direction.append((int(sec), d))

# 이동 방향 바꾸기 [동, 남, 서, 북]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
direction = 0  # 처음에 동쪽을 바라보고 있는 뱀


# 방향 바꾸기 함수
def turn(direction, c):
    if c == "L":
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4

    return direction


def simulate():
    x, y = 0, 0  # 뱀의 첫 위치 - (1, 1)이라서 0, 0으로 함
    data[x][y] = 2  # 뱀이 존재하는 위치는 2로 함
    direction = 0
    time = 0  # 시간
    index = 0  # 다음에 회전할 정보 - change direction
    q = [(x, y)]  # 뱀이 차지하고 있는 위치 (꼬리가 앞쪽이다.)

    while True:
        # 다음에 이동할 위치를 계산한다. next_x, next_y
        nx = x + dx[direction]
        ny = y + dy[direction]

        # 맵을 나가지 않고 and 자신의 몸통과 부딪히지 않아야 한다.
        # (이동을 할 수 있다)
        if 0 <= nx and nx <= n - 1 and 0 <= ny and ny <= n - 1 and data[nx][ny] != 2:
            # 사과가 없는 경우
            if data[nx][ny] == 0:
                data[nx][ny] = 2
                q.append((nx, ny))  # 머리 추가
                px, py = q.pop(0)  # 꼬리 꺼내서
                data[px][py] = 0  # 꼬리 이동
            elif data[nx][ny] == 1:  # 사과 있음
                data[nx][ny] = 2
                q.append((nx, ny))
        else:  # 이동 못함
            time += 1  # 이번 이동 시간 +1
            break

        x, y = nx, ny  # 다음 위치로 머리를 이동한다.
        time += 1  # 시간 증가

        # 시간 증가후에 회전할 시간이면 회전한다.
        if index < cd and time == change_direction[index][0]:
            direction = turn(direction, change_direction[index][1])
            index += 1

    return time


print(simulate())

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
