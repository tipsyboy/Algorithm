# # 1) dfs 구현 1
# import time

# n, m = map(int, input().split())

# data = []
# copied_data = [[0] * m for _ in range(n)]
# virus_list = []  # 초기 바이러스 지점
# rst = 0

# # init input map data and virus list
# for i in range(n):
#     temp = list(map(int, input().split()))

#     for j in range(m):
#         if temp[j] == 2:
#             virus_list.append((i, j))

#     data.append(temp)

# # set direction UDLR
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]


# def get_safe_area():
#     count = 0

#     for i in range(n):
#         for j in range(m):
#             if copied_data[i][j] == 0:
#                 count += 1

#     return count


# def spread_virus(x, y):
#     # 바이러스 4방향 검사
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]

#         # 맵을 나가지 않으면서
#         if nx >= 0 and nx < n and ny >= 0 and ny < m:
#             if copied_data[nx][ny] == 0:  # 빈칸인 곳
#                 copied_data[nx][ny] = 2  # 바이러스 퍼뜨리고
#                 spread_virus(nx, ny)  # 다음 지점부터 다시 바이러스 ㄱㄱ


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


# s = time.time()
# set_walls(0, 0)
# print(rst)
# print(time.time() - s)


# # 2) bfs로 구현한 거

# from itertools import combinations
# from collections import deque
# import time


# def get_safe_area(copied_data):
#     count = 0
#     for i in range(n):
#         for j in range(m):
#             if copied_data[i][j] == 0:
#                 count += 1

#     return count


# # 4. 바이러스를 퍼뜨림
# def spread_virus(walls_set):

#     # 카피 맵 생성
#     copied_data = [[0] * m for _ in range(n)]
#     for i in range(n):
#         for j in range(m):
#             copied_data[i][j] = data[i][j]

#     # 벽 설치
#     for x, y in walls_set:
#         copied_data[x][y] = 1

#     # 바이러스 퍼뜨리기
#     q = deque()
#     for x, y in virus_list:
#         q.append((x, y))

#         while q:
#             now_x, now_y = q.popleft()

#             for i in range(4):
#                 nx = now_x + dx[i]
#                 ny = now_y + dy[i]

#                 if nx >= 0 and nx < n and ny >= 0 and ny < m:
#                     if copied_data[nx][ny] == 0:
#                         copied_data[nx][ny] = 2
#                         q.append((nx, ny))

#     return get_safe_area(copied_data)


# n, m = map(int, input().split())
# data = []
# virus_list = []  # 바이러스
# empty_list = []  # 빈 공간
# rst = 0
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# # 1. 맵을 입력 받기 / 2. 맵의 바이러스 위치와 빈 공간을 저장
# for i in range(n):
#     temp = list(map(int, input().split()))

#     # 초기 맵의 바이러스 위치
#     for j in range(m):
#         if temp[j] == 2:
#             virus_list.append((i, j))
#         elif temp[j] == 0:
#             empty_list.append((i, j))

#     data.append(temp)

# # 3. 벽을 설치한다. - 맵의 빈칸에서 3개 조합
# for walls_set in combinations(empty_list, 3):
#     rst = max(rst, spread_virus(walls_set))


# start = time.time()
# print(rst)
# print(time.time() - start)


# test case


# 4 6
# 0 0 0 0 0 0
# 1 0 0 0 0 2
# 1 1 1 0 0 2
# 0 0 0 0 0 2

# 7 7
# 2 0 0 0 1 1 0
# 0 0 1 0 1 2 0
# 0 1 1 0 1 0 0
# 0 1 0 0 0 0 0
# 0 0 0 0 0 1 1
# 0 1 0 0 0 0 0
# 0 1 0 0 0 0 0
