# 백트래킹(Backtracking) 연습 3
# 중복 허용해서 찾기 - 완전 탐색? - 브루트포스 아님?

import sys

# sys.setrecursionlimit(10000) # 재귀 한도 풀기
n, m = map(int, sys.stdin.readline().split())

result = []


def back_trac(level):
    if level == m:
        print(" ".join(map(str, result)))
        return

    for i in range(1, n + 1):
        result.append(i)  # 방문 경로 넣고
        back_trac(level + 1)  # 해당 노드로 이동해서 재탐색
        result.pop()


back_trac(0)


# # 2) 중복순열
# from itertools import product
