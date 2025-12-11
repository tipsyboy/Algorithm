# Dec 3, Wed 2025
# https://www.acmicpc.net/problem/3197

import sys
from collections import deque

input = sys.stdin.readline
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


R, C = map(int, input().split())
grid = [list(input().rstrip()) for _ in range(R)]
swan = []
q = deque([])
visited = [[False] * C for _ in range(R)]
parent = [i for i in range(R * C)]

for i in range(R):
    for j in range(C):
        if grid[i][j] == "X":
            continue
        if grid[i][j] == "L":
            swan.append((i * C + j))
        for dx, dy in directions:
            nx, ny = i + dx, j + dy
            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                continue
            if visited[nx][ny] or grid[nx][ny] == "X":
                continue
            if find_parent(i * C + j) != find_parent(nx * C + ny):
                union_parent(i * C + j, nx * C + ny)
        q.append((i, j))
        visited[i][j] = True

time = 0
while q:
    # 1. 검사
    if find_parent(swan[0]) == find_parent(swan[1]):
        break
    # 2. 얼음 녹
    for _ in range(len(q)):
        x, y = q.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                continue
            if visited[nx][ny] or grid[nx][ny] != "X":
                continue

            grid[nx][ny] = "."
            visited[nx][ny] = True
            q.append((nx, ny))

    for x, y in q:
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                continue
            if grid[nx][ny] != "X" and find_parent(x * C + y) != find_parent(nx * C + ny):
                union_parent(x * C + y, nx * C + ny)
    time += 1
print(time)

"""
3 2 
L.
XX
.L

1. 초기 q에 물의 위치 추가 - 백조의 위치도 물이다. 
2. 1을 수행하면서 parent[]를 갱신한다. - 초기 물 공간을 연결한다.
3. bfs를 수행하면서 얼음을 녹인다. 
4. '녹은 얼음'에 대해 새로운 길이 생겼으므로 parent[]를 갱신하여 새 물공간을 연결한다. 
5. 만약 백조의 위치가 같은 공간 안에 있으면 만날 수 있는 상태이다. 
"""
