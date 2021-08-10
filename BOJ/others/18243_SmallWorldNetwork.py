import sys

input = sys.stdin.readline
INF = int(1e9)


def small_world_network():
    for i in range(1, n + 1):
        graph[i][i] = 0

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    # for i in range(1, n + 1):
    #     for j in range(1, n + 1):
    #         print("INF", end=" ") if graph[i][j] >= INF else print(graph[i][j], end=" ")
    #     print()

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if graph[i][j] > 6:
                return "Big World!"

    return "Small World!"


n, k = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for _ in range(k):
    a, b = map(int, input().split())

    graph[a][b] = 1
    graph[b][a] = 1

print(small_world_network())


##########################################

# # 2. bfs
# import sys
# from collections import deque

# input = sys.stdin.readline
# INF = int(1e9)


# def bfs(start):
#     visited = [INF] * (n + 1)
#     visited[start] = 0
#     q = deque([start])

#     while q:
#         now = q.popleft()

#         for adj in graph[now]:
#             if visited[adj] == INF:
#                 q.append(adj)
#                 visited[adj] = visited[now] + 1

#     for i in range(1, n + 1):
#         if visited[i] > 6:
#             return False

#     return True


# n, k = map(int, input().split())
# graph = [[] * (n + 1) for _ in range(n + 1)]

# for _ in range(k):
#     a, b = map(int, input().split())

#     graph[a].append(b)
#     graph[b].append(a)

# flag = True
# for i in range(1, n + 1):
#     if not bfs(i):
#         flag = False
#         break

# if flag:
#     print("Small World!")
# else:
#     print("Big World!")