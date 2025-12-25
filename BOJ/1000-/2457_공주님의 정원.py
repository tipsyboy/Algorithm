# https://www.acmicpc.net/problem/2457

import sys

input = sys.stdin.readline


def convert_day(month: int, day: int) -> int:
    return month * 100 + day


N = int(input())
flowers = []
for _ in range(N):
    sm, sd, em, ed = map(int, input().split())
    flowers.append((convert_day(sm, sd), convert_day(em, ed)))

flowers.sort(key=lambda x: (x[0], x[1]))
start, end = 301, 0
idx = 0
ans = 0
while start < 1201 and idx < N:
    while idx < N and flowers[idx][0] <= start:
        if end < flowers[idx][1]:
            end = flowers[idx][1]
        idx += 1

    # 1)
    if start == end:
        break

    ans += 1
    start = end

if start < 1201:
    ans = 0

print(ans)

"""
2457. 공주님의 정원
    - 1)이 빠지면 TLE -> 더이상 전진할 수 없으면 중지해야한다. 아니면 무한루프

    - 날짜를 간단히 하는 테크닉
"""