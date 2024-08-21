# 2024.08.06 TUE
# https://www.acmicpc.net/problem/16218

import sys

input = sys.stdin.readline
DIFF = 50


def game(N, K):
    junie, test_subject_107 = 0, 0

    for _ in range(N):
        A, B = map(int, input().split())

        overpower = junie + int(A * 1.5)
        junie += A
        test_subject_107 += B

        # 한판승
        if junie - test_subject_107 >= DIFF or overpower - test_subject_107 >= DIFF:
            return 1

        # 동시 타격
        if junie >= K and test_subject_107 >= K:
            return 1

        # test_subject_107의 타격
        if test_subject_107 >= K:
            return -1

        # junie 타격
        if junie >= K or overpower >= K:
            return 1

    return 0


N, K = map(int, input().split())
print(game(N, K))
