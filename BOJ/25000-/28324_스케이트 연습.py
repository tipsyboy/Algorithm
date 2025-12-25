# https://www.acmicpc.net/problem/28324

import sys

input = sys.stdin.readline

N = int(input())
V = list(map(int, input().split()))

ans = [0]
for i in range(N - 1, -1, -1):
    ans.append(min(V[i], ans[N - i - 1] + 1))

print(sum(ans))
