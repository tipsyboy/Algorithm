# ### bfs 구현
# from collections import deque


# def bfs(x, y):
#     q = deque([(x, y)])
#     graph[x][y] = 1  # 노드 방문

#     while q:
#         cur_x, cur_y = q.popleft()
#         UDLR = [
#             (cur_x - 1, cur_y),
#             (cur_x + 1, cur_y),
#             (cur_x, cur_y - 1),
#             (cur_x, cur_y + 1),
#         ]

#         for nx, ny in UDLR:
#             if nx >= 0 and nx < n and ny >= 0 and ny < m and graph[nx][ny] != 1:
#                 q.append((nx, ny))
#                 graph[nx][ny] = 1


# n, m = map(int, input().split())

# graph = []
# result = 0
# for i in range(n):
#     graph.append(list(map(int, input())))

# for i in range(n):
#     for j in range(m):
#         if graph[i][j] == 0:
#             bfs(i, j)
#             result += 1


# print(result)


### dfs
def dfs(x, y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1

        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)

        return True

    return False


n, m = map(int, input().split())

graph = []
result = 0
for i in range(n):
    graph.append(list(map(int, input())))

for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1


print(result)


# bfs로도 구현해보기
# 그래프에서 만약에 0인 부분만 탐색한다면, return 값이 필요없다.


# 3 3
# 001
# 010
# 101

# 4 5
# 00110
# 00011
# 11111
# 00000

# 15 14
# 00000111100000
# 11111101111110
# 11011101101110
# 11011101100000
# 11011111111111
# 11011111111100
# 11000000011111
# 01111111111111
# 00000000011111
# 01111111111000
# 00011111111000
# 00000001111000
# 11111111110011
# 11100011111111
# 11100011111111
