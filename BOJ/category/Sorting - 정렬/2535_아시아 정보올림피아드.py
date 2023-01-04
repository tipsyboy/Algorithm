# https://www.acmicpc.net/problem/2535

import sys

input = sys.stdin.readline

N = int(input())
rst = []
for _ in range(N):
    country, num, score = map(int, input().split())
    rst.append((country, num, score))
rst.sort(key=lambda x: x[2], reverse=True)

medals = [0] * N
ans = []
for i in range(N):
    country, num = rst[i][0], rst[i][1]

    if medals[country - 1] >= 2:
        continue
    ans.append((country, num))
    medals[country - 1] += 1
    if len(ans) == 3:
        break
for i in range(len(ans)):
    print(*ans[i])
