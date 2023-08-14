# https://www.acmicpc.net/problem/10813

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

boxes = [i for i in range(1, N + 1)]
for _ in range(M):
    i, j = map(lambda x: int(x) - 1, input().split())
    boxes[i], boxes[j] = boxes[j], boxes[i]

print(*boxes)