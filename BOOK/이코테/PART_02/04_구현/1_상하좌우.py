import sys

input = sys.stdin.readline


n = int(input())
command = list(map(str, input().split()))

x, y = 1, 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
moves = ["L", "R", "U", "D"]

for com in command:
    for i in range(4):
        if com == moves[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if 1 <= nx < n + 1 and 1 <= ny < n + 1:
        x = nx
        y = ny

print(x, y)
