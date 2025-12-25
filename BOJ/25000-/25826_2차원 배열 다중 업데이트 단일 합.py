# https://www.acmicpc.net/problem/25826

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
grid_init = [list(map(int, input().split())) for _ in range(n)]

imos = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    query = list(map(int, input().split()))

    if query[0] == 1:
        c, x1, y1, x2, y2, k = query
        imos[x1][y1] += k
        imos[x1][y2 + 1] -= k
        imos[x2 + 1][y1] -= k
        imos[x2 + 1][y2 + 1] += k
    else:
        c, x1, y1, x2, y2 = query
        for i in range(x2 + 1):
            for j in range(1, y2 + 1):
                imos[i][j] += imos[i][j - 1]

        for i in range(y2 + 1):
            for j in range(1, x2 + 1):
                imos[j][i] += imos[j - 1][i]

        ans = 0
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                ans += grid_init[i][j] + imos[i][j]

print(ans)


"""
25826. 2차원 배열 다중 업데이트 단일 합
    - 'imos법' 이라는 키워드를 알게 되었다.
"""