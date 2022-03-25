# BOJ 16235 나무 재테크

import sys
from collections import deque

input = sys.stdin.readline
directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def spring_summer():
    for i in range(N):
        for j in range(N):
            t_cnt = len(trees[i][j])
            for k in range(t_cnt):
                if trees[i][j][k] <= board[i][j]:
                    board[i][j] -= trees[i][j][k]
                    trees[i][j][k] += 1
                else:
                    for _ in range(k, t_cnt):
                        board[i][j] += trees[i][j].pop() // 2
                    break


def fall():
    for i in range(N):
        for j in range(N):
            for tree_age in trees[i][j]:
                if tree_age % 5:
                    continue
                for d in range(8):
                    ny, nx = i + directions[d][0], j + directions[d][1]

                    if ny < 0 or ny >= N or nx < 0 or nx >= N:
                        continue
                    trees[ny][nx].appendleft(1)


def winter():
    for i in range(N):
        for j in range(N):
            board[i][j] += A[i][j]


N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
board = [[5] * N for _ in range(N)]

trees = [[deque() for _ in range(N)] for __ in range(N)]
for _ in range(M):
    y, x, age = map(int, input().split())
    trees[y - 1][x - 1].append(age)

for _ in range(K):
    spring_summer()
    fall()
    winter()

rst = 0
for i in range(N):
    for j in range(N):
        rst += len(trees[i][j])

print(rst)

"""
    - 어지럽네;;

    - 각 계절마다 함수를 작성해서 시뮬레이션을 돌린다. 
    - 구현이 조금 귀찮은 편에 속하고 봄/여름의 경우 나누기가 애매하므로 합쳐서 구현했다.
"""