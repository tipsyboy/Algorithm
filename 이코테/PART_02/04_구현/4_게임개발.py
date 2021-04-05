# 1단계 왼쪽으로 방향 틀기 [북(0)->서(3)->남(2)->동(1)] 순서
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


n, m = map(int, input().split())  # n*m 맵 생성
x, y, direction = map(int, input().split())  # 캐릭터의 현재 위치(x, y)와 바라보고 있는 방향(direction)

# game_map과 visit_map 생성
visit_map = [[0] * m for i in range(n)]
game_map = []
for i in range(n):
    temp = list(map(int, input().split()))
    game_map.append(temp)

visit_map[x][y] = 1  # 시작 지점 방문
count = 1  # 다른 곳을 방문한 횟수
turn_time = 0  # 회전 횟수

# 좌표 이동 방향 [북, 동, 남, 서]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


while True:
    turn_left()  # 왼쪽으로 한번 돌아서
    nx = x + dx[direction]  # 다음에 가야할 방향의 좌표를 구한다.
    ny = y + dy[direction]  # (next_x, next_y)

    # nx, ny를 검증
    if visit_map[nx][ny] == 0 and game_map[nx][ny] == 0:  # 갈 수 있는 곳이다 (땅이다 and 방문 안했음)
        visit_map[nx][ny] = 1
        x, y = nx, ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1

    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있으면 뒤로 이동한다. - 이미 방문했더라도
        if game_map[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(game_map)
print(visit_map)
print(count)


# 방문 map과 실제 game map을 따로 두어야 하는 이유
