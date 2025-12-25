# https://www.acmicpc.net/problem/2098
"""
2098. 외판원 순회
    4일복습

    dp[cur][vis] = min(dp[cur][vis], dp[nxt][vis | nxt] + W[cur][nxt])


- dp를 INF로 초기화하지 말아야 하는 반례
16
0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 0 1 1 1 1 1 1 1 1 1 1 1 1 1
0 1 1 0 1 1 1 1 1 1 1 1 1 1 1 1
0 1 1 1 0 1 1 1 1 1 1 1 1 1 1 1
0 1 1 1 1 0 1 1 1 1 1 1 1 1 1 1
0 1 1 1 1 1 0 1 1 1 1 1 1 1 1 1
0 1 1 1 1 1 1 0 1 1 1 1 1 1 1 1
0 1 1 1 1 1 1 1 0 1 1 1 1 1 1 1
0 1 1 1 1 1 1 1 1 0 1 1 1 1 1 1
0 1 1 1 1 1 1 1 1 1 0 1 1 1 1 1
0 1 1 1 1 1 1 1 1 1 1 0 1 1 1 1
0 1 1 1 1 1 1 1 1 1 1 1 0 1 1 1
0 1 1 1 1 1 1 1 1 1 1 1 1 0 1 1
0 1 1 1 1 1 1 1 1 1 1 1 1 1 0 1
0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0
"""

import sys

input = sys.stdin.readline
INF = float("inf")


def tsp(cur: int, visited: int) -> int:
    if visited == VISITED_ALL:
        return W[cur][0] if W[cur][0] else INF

    if dp[cur][visited] != None:
        return dp[cur][visited]

    dp[cur][visited] = INF
    for nxt in range(N):
        if visited & (1 << nxt) == 0 and W[cur][nxt] != 0:
            dp[cur][visited] = min(dp[cur][visited], tsp(nxt, visited | (1 << nxt)) + W[cur][nxt])

    return dp[cur][visited]


N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]
dp = [[None] * (1 << N) for _ in range(N)]
print(*dp, sep="\n")
VISITED_ALL = (1 << N) - 1
print(tsp(0, 1))
