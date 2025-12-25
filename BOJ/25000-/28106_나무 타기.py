# 2024.11.01 FRI
# https://www.acmicpc.net/problem/28106

import sys

sys.setrecursionlimit(2500)
input = sys.stdin.readline
DIV = 998_244_353


def tree_jump(cur, depth, ancestor):
    dist[cur] = depth

    for an in ancestor:
        if dist[cur] - dist[an] <= A[an - 1]:
            dp[cur] += dp[an] % DIV

    for adj in tree[cur]:
        ancestor.append(cur)
        tree_jump(adj, depth + 1, ancestor)
        ancestor.pop()


N = int(input())
P = list(map(int, input().split()))
A = list(map(int, input().split()))

dist = [0] * (N + 1)
tree = [[] for _ in range(N + 1)]
root = -1
for c, p in enumerate(P):
    if p == 0:
        root = c + 1
        continue
    tree[p].append(c + 1)

dp = [0] * (N + 1)
dp[root] = 1
tree_jump(root, 0, [])

ans = 0
for i in range(1, N + 1):
    if len(tree[i]) == 0:
        ans += dp[i] % DIV

print(ans % DIV)
