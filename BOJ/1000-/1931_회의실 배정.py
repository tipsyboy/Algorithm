# https://www.acmicpc.net/problem/1931

import sys

input = sys.stdin.readline

N = int(input())
meetings = []
for _ in range(N):
    s, e = map(int, input().split())
    meetings.append((s, e))

meetings.sort(key=lambda x: (x[1], x[0]))

time = 0
ans = 0
for i in range(N):
    s, e = meetings[i]
    if time <= s:
        ans += 1
        time = e
print(ans)