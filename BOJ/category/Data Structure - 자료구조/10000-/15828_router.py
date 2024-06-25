# https://www.acmicpc.net/problem/15828

import sys
from collections import deque

input = sys.stdin.readline

buffer_size = int(input())
buffer = deque([])

while True:
    data = int(input())
    if data == -1:
        break

    if data == 0:
        buffer.popleft()
    elif len(buffer) < buffer_size:
        buffer.append(data)

print(*buffer) if buffer else print("empty")
