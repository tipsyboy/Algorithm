# # 1.
# from collections import deque


# def bfs(n, k):
#     if n == k:
#         return 0

#     q = deque()
#     q.append((n, 0))  # 시작점 deque에 추가 (좌표, 시간)
#     visited[n] = True  # 시작점 방문처리

#     while q:
#         x, sec = q.popleft()

#         for nx in (x-1, x+1, x*2):
#             if nx == k:
#                 return sec + 1

#             if 0 <= nx <= MAX and not visited[nx]:
#                 q.append((nx, sec+1))
#                 visited[nx] = True


# n, k = map(int, input().split())
# MAX = 10 ** 5
# visited = [False] * (MAX+1)

# print(bfs(n, k))


# 2.
from collections import deque


def bfs(n, k):
    q = deque([n])

    while q:
        x = q.popleft()

        if x == k:
            return sec[x]

        for nx in (x-1, x+1, x*2):
            if 0 <= nx <= MAX and not sec[nx]:
                q.append(nx)
                sec[nx] = sec[x] + 1


n, k = map(int, input().split())
MAX = 100000
sec = [0] * (MAX + 1)

print(bfs(n, k))
