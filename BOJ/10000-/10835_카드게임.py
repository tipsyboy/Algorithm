# 2025.01.17 FRI
# https://www.acmicpc.net/problem/10835


import sys

input = sys.stdin.readline
sys.setrecursionlimit(4500)


def card_game(left, right):
    if left == N or right == N:
        return 0

    if dp[left][right] != -1:
        return dp[left][right]

    left_card = A[left]
    right_card = B[right]

    if right_card < left_card:
        dp[left][right] = max(dp[left][right], card_game(left, right + 1) + right_card)
    else:
        dp[left][right] = max(card_game(left + 1, right), card_game(left + 1, right + 1))

    return dp[left][right]


N = int(input())
A = list(map(int, input().split()))  # left cards
B = list(map(int, input().split()))  # right cards
dp = [[-1] * N for _ in range(N)]
print(card_game(0, 0))

"""
10835. 카드게임
    - MLE, TLE를 피하기.
    - TLE의 경우 -> 오른쪽 카드를 제거 했을 때만 점수를 얻을 수 있으므로 오른쪽 카드를 제거할 수 있는 상황은 오른쪽 카드만 제거하는 것이 이득이다. 가지치기
    - MLE의 경우 
      -> 파이썬은 기본적으로 재귀 깊이 1000까지고 더 넓혀줄 수 있다. 이 경우 4000까지로 보는 것이 맞으나, 4000일때도 실패한다. 
         이유는 파이썬 재귀를 사용하고 하는데 내부적으로 5정도의 깊이가 필요함. 따라서 4005를 하던지 넉넉하게 4500정도 잡는다.
"""
