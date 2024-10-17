# 2024.10.11 FRI
# https://www.acmicpc.net/problem/25711

import sys

input = sys.stdin.readline


def get_dist(s, e):
    x1, y1 = s
    x2, y2 = e

    return (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5


def cal_slope(s, e):
    _, y1 = s
    _, y2 = e

    if y1 == y2:
        return 0

    return 1 if y2 > y1 else -1


N, Q = map(int, input().split())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))

go = [0]
back = [0]
for p in range(N - 1):
    s, e = (X[p], Y[p]), (X[p + 1], Y[p + 1])
    dist = get_dist(s, e)
    slope = cal_slope(s, e)
    if slope > 0:
        go.append(go[-1] + dist * 3)
        back.append(back[-1] + dist)
    elif slope < 0:
        go.append(go[-1] + dist)
        back.append(back[-1] + dist * 3)
    else:
        go.append(go[-1] + dist * 2)
        back.append(back[-1] + dist * 2)


ans = []
for _ in range(Q):
    i, j = map(int, input().split())

    if i < j:
        ans.append(go[j - 1] - go[i - 1])
    else:
        ans.append(back[i - 1] - back[j - 1])

for a in ans:
    print(f"{a:.4f}")
