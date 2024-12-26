# 2024.12.01 SUN
# https://www.acmicpc.net/problem/1135

import sys

input = sys.stdin.readline


def dfs(cur):
    if not tree[cur]:
        return 0

    rst = []  # 자식노드가 전파에 걸리는 시간 결과값
    for child in tree[cur]:
        rst.append(dfs(child))
    rst.sort(reverse=True)  # 자식이 많은 노드부터 전파하는 것이 이득이다.

    times = []
    for gone, sub in enumerate(rst):
        times.append(sub + gone + 1)  # 자식이 전파에 걸리는 시간 + 지나간 시간 + 자식에게 전파하는 시간 1분

    return max(times)


N = int(input())
parent = list(map(int, input().split()))
tree = [[] for _ in range(N)]
for c, p in enumerate(parent):
    if p == -1:
        continue
    tree[p].append(c)

print(dfs(0))
