def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")

    # adjacent node
    for node in graph[v]:  # 현재 노드의 인접노드를 순회 하면서
        if not visited[node]:  # 그 인접 노드를 방문 하지 않았다면
            dfs(graph, node, visited)  # 노드 방문


# 0번 노드도 넣어줘~
graph = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]
visited = [False] * 9

dfs(graph, 1, visited)
