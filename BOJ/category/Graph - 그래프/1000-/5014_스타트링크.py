import sys
from collections import deque


input = sys.stdin.readline


def BFS(start, dest) -> int:
    q = deque([start])
    visited = [-1] * (F + 1)
    visited[start] = 0

    while q:
        now = q.popleft()

        if now == dest:
            return visited[now]

        for move in [U, -D]:
            nxt = now + move
            if nxt < 1 or nxt > F or visited[nxt] != -1:
                continue

            visited[nxt] = visited[now] + 1
            q.append(nxt)

    return -1


F, S, G, U, D = map(int, input().split())  # F:총 층수, S:시작, G:도착지, U:올라가는 층, D:내려가는 층
rst = BFS(S, G)

if rst != -1:
    print(rst)
else:
    print("use the stairs")
