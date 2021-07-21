import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline


def check_safe_area(virus_map):
    count = 0

    for i in range(row):
        for j in range(col):
            if virus_map[i][j] == 0:
                count += 1

    return count


def spread_virus(graph, empty):
    # copied_graph = copy.deepcopy(graph)  # copy the graph
    # copy the graph
    copied_graph = [[0] * col for _ in range(row)]
    for i in range(row):
        for j in range(col):
            copied_graph[i][j] = graph[i][j]

    # 벽 세우기
    for i, j in empty:
        copied_graph[i][j] = 1

    # directions
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for start_x, start_y in virus:
        q = deque([(start_x, start_y)])

        while q:
            x, y = q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < row and 0 <= ny < col:
                    if copied_graph[nx][ny] == 0:
                        q.append((nx, ny))
                        copied_graph[nx][ny] = 2

    return check_safe_area(copied_graph)


# main
row, col = map(int, input().split())
graph = []
virus = []  # virus 위치
empty_area = []  # 빈 공간의 위치
rst = 0

for i in range(row):
    temp = list(map(int, input().split()))

    for j in range(col):
        if temp[j] == 2:
            virus.append((i, j))
        elif temp[j] == 0:
            empty_area.append((i, j))

    graph.append(temp)


for empty_pos in combinations(empty_area, 3):
    rst = max(rst, spread_virus(graph, empty_pos))

print(rst)


# 벽 세우기
# def set_walls(start, count):
#     global rst
#     # 벽이 세개인 경우
#     if count == 3:
#         # 바이러스가 퍼지는 시뮬레이션을 하기위해서 맵을 복사
#         for i in range(n):
#             for j in range(m):
#                 copied_data[i][j] = data[i][j]

#         # 바이러스를 퍼뜨림 - 초기 바이러스 위치 x, y부터 바이러스 발사~
#         for x, y in virus_list:
#             spread_virus(x, y)

#         # 바이러스를 맵에 갈수있는 곳에 전부 보내고 난 뒤에
#         rst = max(rst, get_safe_area())

#         return

#     # 벽을 세우는 경우
#     for i in range(start, n * m):
#         x = i // m
#         y = i % m

#         if data[x][y] == 0:
#             data[x][y] = 1
#             count += 1
#             set_walls(i + 1, count)
#             data[x][y] = 0
#             count -= 1


"""
26. 14502 연구소 (Gold 5)
    - 복합적인 문제 
      1) 바이러스를 퍼뜨리기 위해서 bfs, 
      2) 벽 세개를 세워서 안전지대를 체크하기 위해서 brute-force,
      3) 벽을 세울 수 있는 경우의 수를 조합하기 위해 백트래킹 (위 코드에서는 itertools의 combinations을 사용했다.)
      을 사용하는 문제이다. 

    - spread_virus()는 전형적인 bfs로 해결

    - 벽 세개를 세워서 안전지대를 찾는 과정은 모든 경우의 수에서 0의 개수를 전부 세줘야 하므로 브루트포스로 해야한다. 

    - 3개의 벽을 세우는 과정은 combinations를 사용함.

    - 첫 시도때 deepcopy를 통해서 바이러스를 퍼뜨릴 copied_map을 생성했는데, for loop로 직접 복사하는 경우보다
      상당히 느리게 수행되는 것을 볼 수 있었다.
      
      구글링을 해보니까 deepcopy가 파이썬의 슬라이싱이나 for loop를 통한 직접 복사보다 상당히 느리다는 사실을 알게되었다. 
"""
