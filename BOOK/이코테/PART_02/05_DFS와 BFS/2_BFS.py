from collections import deque


def bfs(graph, start, visited):
    queue = deque([start])  # 시작 노드로 큐를 생성
    visited[start] = True  # 현재 노드 방문

    # queue가 빌 때까지 반복
    while queue:
        v = queue.popleft()
        print(v, end=" ")

        for node in graph[v]:
            if not visited[node]:
                queue.append(node)
                visited[node] = True


graph = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]
visited = [False] * 9

bfs(graph, 1, visited)
