# https://www.acmicpc.net/problem/10971

"""
10971. 외판원 순회 2
    - TSP 알고리즘 분류가 따로 있으며, 이 코드는 브루트포스로 해결했지만 DP에 기록한다.

    - 모든 경우의 수를 찾는다.
"""


import sys

input = sys.stdin.readline
INF = float("inf")


def tsp(start: int, now: int, visited: int, dist: int) -> None:
    global ans

    if visited == VISITED_ALL:
        to_home = W[now][start] or INF  # 이렇게도 쓸 수 있었네
        # to_home = W[now][start] if W[now][start] else INF
        ans = min(ans, dist + to_home)
        return

    for nxt in range(N):
        if visited & (1 << nxt) == 0 and W[now][nxt] != 0:  # (방문 확인 / 지금 노드에서 갈 수 없는)
            tsp(start, nxt, visited | (1 << nxt), dist + W[now][nxt])


N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]

ans = INF
VISITED_ALL = (1 << N) - 1
tsp(0, 0, 1, 0)
print(ans)
