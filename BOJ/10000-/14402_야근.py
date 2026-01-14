# Aug 8, 2025 Fri
# https://www.acmicpc.net/problem/14402

import sys
from collections import defaultdict

input = sys.stdin.readline

q = int(input())
attendance = defaultdict(int)
ans = 0
for _ in range(q):
    s, p = input().split()

    if p == "+":
        attendance[s] += 1
    else:
        if attendance[s]:
            attendance[s] -= 1
        else:
            ans += 1

ans += sum(v for v in attendance.values())
print(ans)
