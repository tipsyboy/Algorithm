# https://www.acmicpc.net/problem/10655

"""
10655. 마라톤 1
    - 매번 건너뛰는 포인트 i번째를 제외하고 계산하면 TLE를 받는다. 

    - 시작점부터 모든 포인트의 거리를 누적합으로 구해놓고, i번째를 제외 시키면서 최소 택시거리를 찾는다.
"""

import sys

input = sys.stdin.readline
INF = float("inf")


def taxi_dist(s: tuple, d: tuple) -> int:
    return abs(s[0] - d[0]) + abs(s[1] - d[1])


N = int(input())
check_point = []
for _ in range(N):
    x, y = map(int, input().split())
    check_point.append((x, y))

dist = [0]
for i in range(N - 1):
    dist.append(taxi_dist(check_point[i], check_point[i + 1]) + dist[-1])

ans = INF
for a in range(1, N - 1):
    temp = dist[a - 1] + (dist[N - 1] - dist[a + 1])
    temp += taxi_dist(check_point[a - 1], check_point[a + 1])

    ans = min(ans, temp)

print(ans)
