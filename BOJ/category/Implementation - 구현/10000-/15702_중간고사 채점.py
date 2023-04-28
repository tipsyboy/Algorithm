# https://www.acmicpc.net/problem/15702

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
points = list(map(int, input().split()))

student, maxv = -1, -1
for _ in range(M):
    num, *board = input().split()

    temp = 0
    for i in range(N):
        if board[i] == "O":
            temp += points[i]

    if temp > maxv:
        student = int(num)
        maxv = temp
    elif temp == maxv:
        student = min(student, int(num))

print(student, maxv)
