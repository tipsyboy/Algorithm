from collections import deque


# bfs 구현
def bfs(graph, v):  # graph, start node
    visited = [False] * (n+1)  # check visited node
    count = 0  # counting virus pc

    # node v: start node
    q = deque([v])
    visited[v] = True

    while q:
        now = q.popleft()

        # check adjacent node
        for node in graph[now]:
            if not visited[node]:
                q.append(node)
                visited[node] = True
                count += 1

    return count


def dfs(graph, v, visited):
    global count

    visited[v] = True
    # count += 1  # 여기 두면 1번 노드까지 카운트를 함

    for i in graph[v]:
        if not visited[i]:
            count += 1
            dfs(graph, i, visited)


n = int(input())  # node
e = int(input())  # edge
graph = [[] for _ in range(n+1)]

# 무방향 그래프
for _ in range(e):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)


# print(bfs(graph, 1))

# dfs 구현
visited = [False] * (n + 1)
count = 0
dfs(graph, 1, visited)
print(count)
