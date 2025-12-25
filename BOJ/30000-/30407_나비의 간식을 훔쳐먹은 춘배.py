# 2024.09.29 SUN
# https://www.acmicpc.net/problem/30407

import sys

input = sys.stdin.readline
INF = float("inf")


def nyang(turn, dist, ast):
    if turn == N:
        return 0

    if dp[turn][dist][ast] != INF:
        return dp[turn][dist][ast]

    # 1. 이전 턴 깜짝 놀라게 하기 사용
    if ast == 1:
        rst = nyang(turn + 1, dist + K, 2)  # 이번턴 데미지를 받지 않으니 웅크리기는 의미X
    else:
        # 2. 웅크리기
        d1 = nyang(turn + 1, dist, ast) + max(0, (R[turn] - dist) // 2)  # 다음 턴 수행 + 이번 턴 데미지

        # 3. 기어가기
        d2 = nyang(turn + 1, dist + K, ast) + max(0, R[turn] - (dist + K))
        rst = min(d1, d2)

        # 4. 깜짝 놀라게하기 - 0: 사용X, 1: 이전 턴 사용, 2: 사용O
        if ast == 0:
            rst = min(rst, nyang(turn + 1, dist, 1) + max(0, R[turn] - dist))

    dp[turn][dist][ast] = rst
    return dp[turn][dist][ast]


N = int(input())
H, D, K = map(int, input().split())
R = list(int(input()) for _ in range(N))


dp = [[[INF] * 3 for _ in range(D + N * K)] for __ in range(N)]
ans = H - nyang(0, D, 0)
if ans <= 0:
    ans = -1
print(ans)
