# 2024.08.31 SAT
# https://www.acmicpc.net/problem/31823

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

ans = set()
ans_name = []
for _ in range(N):
    v = input().split()
    streak, name = v[:-1], v[-1]

    rst = cnt = 0
    for grass in streak:
        if grass == ".":
            cnt += 1
        else:
            rst = max(rst, cnt)
            cnt = 0

    rst = max(rst, cnt)
    ans.add(rst)
    ans_name.append((rst, name))

print(len(ans))
for i in range(N):
    print(*ans_name[i])
