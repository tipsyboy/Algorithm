import sys
from collections import deque

input = sys.stdin.readline
MAX = 10 ** 5


def bfs(start, dest):
    q = deque([start])
    visited = [-1] * (MAX + 1)
    visited[start] = 0

    move = [-1, -a, -b, 1, a, b]

    while q:
        now = q.popleft()

        if now == dest:
            return visited[dest]

        # 더하기 빼기 이동
        for i in range(6):
            nxt = now + move[i]

            if 0 <= nxt <= MAX and visited[nxt] == -1:
                q.append(nxt)
                visited[nxt] = visited[now] + 1

        # 곱 이동
        for i in [a, b]:
            nxt = now * i

            if 0 <= nxt <= MAX and visited[nxt] == -1:
                q.append(nxt)
                visited[nxt] = visited[now] + 1

    return vistied[dest]


a, b, n, m = map(int, input().split())
print(bfs(n, m))
