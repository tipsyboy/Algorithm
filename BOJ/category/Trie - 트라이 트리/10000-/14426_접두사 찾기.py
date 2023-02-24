# https://www.acmicpc.net/problem/14426
# 복습이 필요함

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
prefix = set()
for _ in range(N):
    word = input().rstrip()

    for i in range(1, len(word) + 1):
        prefix.add(word[:i])

ans = 0
for _ in range(M):
    candidate = input().rstrip()
    if candidate in prefix:
        ans += 1

print(ans)

"""
14426. 접두사 찾기
    - 0. Feb.24.2023 기준으로 난이도가 S1이나 생각해볼게 많은것 같은 문제.

    - 1. 트라이 트리 연습문제로 나왔으나
      N개의 단어에서 나올 수 있는 모든 접두사를 set()으로 관리하고 숫자를 세주는 식으로 풀이 했음.
      풀이를 할 때는 O(NL+M) 으로 생각하고 풀었고, 간당간당하게 통과가 되긴했음. (1776ms - python3)

    - 2. 트라이 트리로 해보기

    - 3. 이분탐색 풀이가 있던데 잘 모르겠는데...?
"""