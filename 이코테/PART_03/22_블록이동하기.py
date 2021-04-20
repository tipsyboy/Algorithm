from collections import deque


def get_next_position(pos, board):
    n = len(board)  # 맵 크기

    # {(x1, y1), (x2, y2)}
    pos = list(pos)
    pos1_x, pos1_y, pos2_x, pos2_y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
    next_positions = []

    # 1. 이번턴 이동하는 경우 - 상하좌우 4방향 검사
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        pos1_nx = pos1_x + dx[i]
        pos1_ny = pos1_y + dy[i]
        pos2_nx = pos2_x + dx[i]
        pos2_ny = pos2_y + dy[i]

        # 맵을 안 벗어나고, 벽이 아니면 좌표를 추가
        if pos1_nx >= 0 and pos1_nx < n and pos1_ny >= 0 and pos1_ny < n:
            if pos2_nx >= 0 and pos2_nx < n and pos2_ny >= 0 and pos2_ny < n:
                if board[pos1_nx][pos1_ny] != 1 and board[pos2_nx][pos2_ny] != 1:
                    next_positions.append({(pos1_nx, pos1_ny), (pos2_nx, pos2_ny)})

    # 2. 이번턴 회전 하는 경우
    # 축이 되는 좌표는 놔두고 회전함

    # 2-1. 두 점이 가로로 놓여 있는 경우 - 행 좌표가 같은 경우
    if pos1_x == pos2_x:
        for i in [-1, 1]:
            pos_nx = pos1_x + i  # pos1_x와 pos2_x가 같기 때문에 하나만

            # 맵을 벗어 나지 않고,
            if pos_nx >= 0 and pos_nx < n:
                if board[pos_nx][pos1_y] != 1 and board[pos_nx][pos2_y] != 1:
                    next_positions.append({(pos1_x, pos1_y), (pos_nx, pos1_y)})
                    next_positions.append({(pos2_x, pos2_y), (pos_nx, pos2_y)})
    # 2-2. 두 점이 세로로 놓여 있는 경우 - 열 좌표가 같은 경우
    elif pos1_y == pos2_y:
        for i in [-1, 1]:
            pos_ny = pos1_y + i  # pos1_y와 pos2_y가 같기 때문에 하나만

            if pos_ny >= 0 and pos_ny < n:
                if board[pos1_x][pos_ny] != 1 and board[pos2_x][pos_ny] != 1:
                    next_positions.append({(pos1_x, pos1_y), (pos1_x, pos_ny)})
                    next_positions.append({(pos2_x, pos2_y), (pos2_x, pos_ny)})

    return next_positions


def solution(board):
    n = len(board)  # map의 크기 (n * n) map
    pos = {(0, 0), (0, 1)}  # 처음 위치 - set으로 저장해서 이전에 방문 한 곳을 중복 방지한다.(좌표를 두개씩 차지하기 때문)
    visited = [pos]
    q = deque([(pos, 0)])  # 방문위치와 시간 cost를 저장 (position, cost)

    while q:
        pos, cost = q.popleft()

        # 현재 위치가 마지막 좌표를 갖고 있으면 도착지점 도달
        if (n - 1, n - 1) in pos:
            return cost

        # 현재 위치에서 이동할 수 있는 좌표 탐색 (맵을 벗어나지 않고 벽에 부딪히지 않으면)
        for next_pos in get_next_position(pos, board):
            # 탐색한 좌표가 방문하지 않은 좌표라면 (위에서 한번 걸러낸 좌표를 방문하지 않았으면)
            if next_pos not in visited:
                # queue에 추가하고 방문처리한다. (차례가 오면 그 곳으로 이동할 것임)
                q.append((next_pos, cost + 1))  # 시간까지 같이 추가
                visited.append(next_pos)

    # 완전 탐색 이후 목표 지점에 도달하지 못한 경우
    # 하지만 문제에서 목표지점에 도달할 수 있는 경우만 테스트케이스로 주어지므로
    # 사실상 필요없다.
    return -1


print(
    solution(
        [
            [0, 0, 0, 1, 1],
            [0, 0, 0, 1, 0],
            [0, 1, 0, 1, 1],
            [1, 1, 0, 0, 1],
            [0, 0, 0, 0, 0],
        ]
    )
)
