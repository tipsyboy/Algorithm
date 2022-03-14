import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

# 8방향 이동
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]


# 물고기의 이동
def move_all_fishes(graph, sx, sy):
    def find_fish(x):
        for i in range(4):
            for j in range(4):
                if graph[i][j][0] == x:
                    return (i, j)

        return None  # x번 물고기 없음

    # 물고기는 1~16번 차례대로 이동한다.
    for i in range(1, 17):
        fish_pos = find_fish(i)  # i번 물고기 찾기

        if fish_pos == None:  # 물고기를 못찾음
            continue

        x, y = fish_pos
        direction = graph[x][y][1]  # 물고기 방향

        # 한 물고기는 최대 8방향까지 바꿔가면서 이동할 자리를 찾는다.
        for j in range(8):
            nx = x + dx[direction]
            ny = y + dy[direction]

            if 0 <= nx < 4 and 0 <= ny < 4:
                if not (nx == sx and ny == sy):  # 상어가 있으면 못감
                    graph[x][y] = (i, direction)  # 물고기의 방향을 바뀐 방향으로 갱신
                    graph[x][y], graph[nx][ny] = graph[nx][ny], graph[x][y]  # 자리 바꾸기
                    break

            # 이번 방향으로 자리 이동을 못하면 방향을 바꾼다.
            direction = (direction + 1) % 8


# 상어가 이동할 수 있는 좌표를 얻는 함수
def get_next_pos(graph, sx, sy):
    next_pos = []
    direction = graph[sx][sy][1]  # 상어의 방향

    # 4x4 map에서 최대 3개까지 이동가능한 좌표가 나온다.
    for i in range(1, 4):
        nx = sx + dx[direction] * i
        ny = sy + dy[direction] * i

        if 0 <= nx < 4 and 0 <= ny < 4:
            if graph[nx][ny][0] != -1:  # 상어는 물고기가 있는곳만 갈 수 있다.
                next_pos.append((nx, ny))

    return next_pos


# 상어가 물고기를 먹음
def eat_fish(graph, fish_cnt, sx, sy):
    global rst

    # 이번회차 map의 상태 - 재귀로 map의 상태가 계속 바뀌므로 이번회차의 map의 상태를 저장한다.
    now_graph = [[None] * 4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            now_graph[i][j] = graph[i][j]

    # 상어가 물고기를 먹음
    # 상어가 먹은 물고기의 방향을 갖게되므로 방향은 그대로 저장한다.
    fish_cnt += now_graph[sx][sy][0]
    now_graph[sx][sy] = (-1, now_graph[sx][sy][1])
    # 이제 물고기가 이동한다.
    move_all_fishes(now_graph, sx, sy)

    # 상어가 이동할 차례인데, 상어는 방향의 모든 지역을 갈 수 있기 때문에 찾아야함.
    nxt_pos = get_next_pos(now_graph, sx, sy)

    # 이동이 불가능한 경우
    if not nxt_pos:
        rst = max(rst, fish_cnt)
        return

    # 다음 좌표로 상어 이동
    for nx, ny in nxt_pos:
        eat_fish(now_graph, fish_cnt, nx, ny)


# 초기 map data
graph = [[] * 4 for _ in range(4)]
for i in range(4):
    temp = list(map(int, input().split()))  # 행을 받아서
    for j in range(4):  # 2개 data씩 자른다.
        # (물고기번호, 방향) 방향은 dx, dy와 매칭을 위해 -1
        graph[i].append((temp[2 * j], temp[2 * j + 1] - 1))

rst = 0
eat_fish(graph, 0, 0, 0)
print(rst)
