# 2024.07.17 WED
# https://www.acmicpc.net/problem/12993

import sys
from collections import deque

input = sys.stdin.readline

x, y = map(int, input().split())

q = deque([(0, 0)])
k = 0
ans = False
while q:
    move = 3**k
    for _ in range(len(q)):
        cx, cy = q.popleft()

        if cx == x and cy == y:
            ans = True

        for dx, dy in [(move, 0), (0, move)]:
            nx, ny = cx + dx, cy + dy

            if nx > x or ny > y:
                continue

            q.append((nx, ny))
    k += 1

print(1) if ans else print(0)
