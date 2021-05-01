# # 1) bfs 구현
# import sys
# from collections import deque
# input = sys.stdin.readline

# t = int(input())

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# for _ in range(t):
#     m, n, k = map(int, input().split())  # 맵 가로 / 맵 세로 / 배추 수
#     cabbages = deque()  # 배추 좌표
#     count = 0  # 필요한 배추 흰지렁이

#     # 배추 위치
#     for _ in range(k):
#         a, b = map(int, input().split())
#         cabbages.append((a, b))  # 배추 위치 저장

#     # for bfs
#     q = deque()

#     while cabbages:
#         q.append(cabbages.popleft())

#         while q:
#             x, y = q.popleft()

#             for i in range(4):
#                 nx = x + dx[i]
#                 ny = y + dy[i]

#                 if nx >= 0 and nx < m and ny >= 0 and ny < n:
#                     if (nx, ny) in cabbages:
#                         q.append((nx, ny))
#                         cabbages.remove((nx, ny))

#         count += 1

#     print(count)


# 2) set으로 자료형을 바꿔서 in 연산할때 속도 증가
import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(t):
    m, n, k = map(int, input().split())  # 맵 가로 / 맵 세로 / 배추 수
    cabbages = set()  # 배추 좌표
    count = 0  # 필요한 배추 흰지렁이

    # 배추 위치
    for _ in range(k):
        a, b = map(int, input().split())
        cabbages.add((a, b))  # 배추 위치 저장

    # for bfs
    q = deque()

    while cabbages:
        q.append(cabbages.pop())

        while q:
            x, y = q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx >= 0 and nx < m and ny >= 0 and ny < n:
                    if (nx, ny) in cabbages:
                        q.append((nx, ny))
                        cabbages.remove((nx, ny))

        count += 1

    print(count)
