# https://www.acmicpc.net/problem/2780

import sys

input = sys.stdin.readline
DIV = 1_234_567
MAX_N = 1000


adj_nums = [[7], [2, 4], [1, 3, 5], [2, 6], [1, 5, 7], [2, 4, 6, 8], [3, 5, 9], [0, 4, 8], [5, 7, 9], [6, 8]]
password = [[0] * 10 for _ in range(MAX_N)]
password[0] = [1 for _ in range(10)]
for i in range(1, MAX_N):
    for j in range(10):
        for adj in adj_nums[j]:
            password[i][j] += password[i - 1][adj] % DIV

T = int(input())
for _ in range(T):
    N = int(input())
    print(sum(password[N - 1]) % DIV)
