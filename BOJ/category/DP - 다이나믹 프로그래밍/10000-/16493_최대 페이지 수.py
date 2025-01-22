# 2025.01.09 THU
# https://www.acmicpc.net/problem/16493

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
chapters = [tuple(map(int, input().split())) for _ in range(M)]

dp = [[0] * (N + 1) for _ in range(M)]
days, pages = chapters[0]
if days <= N:
    dp[0][N - days] = pages
for i in range(1, M):
    days, pages = chapters[i]
    for j in range(N + 1):
        if j <= N - days:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j + days] + pages)
        else:
            dp[i][j] = dp[i - 1][j]

print(max(dp[M - 1]))


# - 조건
# 각 챕터는 독립적이다.
# 한 챕터를 시작하면 days 만큼 시간을 쏟아야한다. 중간에 그만읽기 불가
# 냅색?

# - 상태
# i번 째 챕터를 읽는다. / 읽지 않는다.

# dp 테이블 구성하기
# dp[i][j] = i번 챕터까지 존재한다 할때, 남은 일수가 j인 상태에서의 최적값. < 문제의 조건의 N 즉, 날짜의 최대 값이 200으로 매우 작다.
