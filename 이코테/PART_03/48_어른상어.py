import sys

input = sys.stdin.readline

# 4방향 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 냄새 관리 함수
def update_smell_map(graph, smell_map):
    for i in range(n):
        for j in range(n):
            # 이미 냄새가 뿌려져 있는 경우 - 냄새 뿌리기보다 먼저 수행한다.
            if smell_map[i][j][0] != 0:
                smell_map[i][j][1] -= 1

                # 시간이 지나 냄새가 사라진 경우
                if smell_map[i][j][1] == 0:
                    smell_map[i][j][0] = 0  # 지역의 냄새 정보를 초기화한다.

            # (i, j) 좌표에 현재 상어가 있는 경우 - 냄새 뿌리기
            if graph[i][j] != 0:
                smell_map[i][j] = [graph[i][j], k]


# 상어의 이동
def move_all_sharks(graph, smell_map):
    # 상어가 이동할 때, 상어간 이동 우선순위는 없기 때문에 기존의 그래프를 그대로 사용하면
    # 아직 이동하지 않은 상어와 겹치면서 상어가 소멸할 가능성이 생긴다.
    # 또한, 이미 이동한 상어가 그래프 탐색중에 다시 만나서 또 이동하는 경우도 생길 수 있다.
    # 따라서 상어의 이동을 위한 임시 이동 맵을 하나 생성한다.
    temp_graph = [[0] * n for _ in range(n)]
    move_count = 0

    # 상어의 이동에는 순서가 없으므로 map을 차례로 탐색하면서 이동한다.
    # 하지만 상어가 겹치는 경우 낮은 번호 상어만 유지한다.
    for i in range(n):
        for j in range(n):
            if move_count == m:
                return temp_graph

            if graph[i][j] != 0:  # 맵에 상어가 있는 경우
                move_count += 1
                direction = directions[graph[i][j] - 1]  # 현재 상어의 방향
                flag = False  # 이번 상어가 빈칸으로 이동

                # 두 경우 모두 후보가 여러개일수 있으므로, 우선순위대로 탐색한다.
                get_priority = priority[graph[i][j] - 1][direction - 1]

                # 1) 먼저 냄새가 없는 지역을 탐색한다. - 4방향 탐색
                for d in range(4):
                    # 위에서 구한 우선순위 차례대로 탐색
                    nx = i + dx[get_priority[d] - 1]
                    ny = j + dy[get_priority[d] - 1]

                    if 0 <= nx < n and 0 <= ny < n:
                        if smell_map[nx][ny][0] == 0:  # 후보 지역에 냄새가 없다.
                            # 그쪽으로 머리를 돌려서 이동해야함.
                            directions[graph[i][j] - 1] = get_priority[d]

                            # 그런데, 가려는 지역에 이미 상어가 있는 경우
                            if temp_graph[nx][ny] != 0:
                                temp_graph[nx][ny] = min(
                                    temp_graph[nx][ny], graph[i][j]
                                )
                            else:  # 상어가 없음 - 이동
                                temp_graph[nx][ny] = graph[i][j]

                            flag = True
                            break

                if flag:  # 1)의 경우로 상어가 이동함
                    continue

                # 2) 인접지역에 빈칸이 없어, 자기 냄새쪽으로 가려한다.
                for d in range(4):
                    nx = i + dx[get_priority[d] - 1]
                    ny = j + dy[get_priority[d] - 1]

                    if 0 <= nx < n and 0 <= ny < n:
                        if smell_map[nx][ny][0] == graph[i][j]:  # 내 냄새다.
                            # 그쪽으로 머리를 돌려서 이동해야함.
                            directions[graph[i][j] - 1] = get_priority[d]

                            # 이 경우는 미리 상어가 와있을리가 없음 - 자기 냄새쪽으로 이동
                            temp_graph[nx][ny] = graph[i][j]
                            break

    return temp_graph


def check_map(graph):
    for i in range(n):
        for j in range(n):
            if graph[i][j] > 1:
                return False

    return True


def simulation(graph, smell_map):
    time = 0

    while True:
        # 냄새 업데이트
        update_smell_map(graph, smell_map)

        # 상어의 이동
        graph = move_all_sharks(graph, smell_map)

        # 1s
        time += 1

        if check_map(graph):
            return time

        if time >= 1000:
            return -1


n, m, k = map(int, input().split())  # 맵 크기 / 상어의 수 / 냄새 지속시간
graph = [list(map(int, input().split())) for _ in range(n)]

directions = list(map(int, input().split()))  # 상어의 방향

priority = [[] * m for _ in range(m)]

# 상어의 이동 우선순위
for i in range(m):
    for j in range(4):
        priority[i].append(list(map(int, input().split())))

# 냄새 관리 리스트
smell_map = [[[0, 0]] * n for _ in range(n)]  # [냄새 주인 상어, 남은 지속시간]

print(simulation(graph, smell_map))
