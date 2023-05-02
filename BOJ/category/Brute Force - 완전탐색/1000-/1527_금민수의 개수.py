# https://www.acmicpc.net/problem/1527

import sys
from collections import deque

input = sys.stdin.readline

A, B = map(int, input().split())
q = deque([""])
ans = 0
while True:
    flag = False
    now = q.popleft()
    for fs in ["4", "7"]:
        nxt = now + fs
        if A <= int(nxt) <= B:
            ans += 1
        elif int(nxt) > B:
            flag = True
            break
        q.append(nxt)
    if flag:
        break

print(ans)