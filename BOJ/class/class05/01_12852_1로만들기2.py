from collections import deque


def bfs(start):
    arr = [0] * (n + 1)
    q = deque([(start, [start])])
    visited = [False] * (n + 1)
    visited[start] = True

    while q:
        now, route = q.popleft()

        if now == 1:
            return route

        if now % 3 == 0 and not visited[now // 3]:
            q.append((now // 3, route + [now // 3]))
            visited[now // 3] = True

        if now % 2 == 0 and not visited[now // 2]:
            q.append((now // 2, route + [now // 2]))
            visited[now // 2] = True

        if not visited[now - 1]:
            q.append((now - 1, route + [now - 1]))
            visited[now - 1] = True


n = int(input())
q = deque([[n, [n]]])
rst = bfs(n)
print(len(rst) - 1)
print(*rst)
