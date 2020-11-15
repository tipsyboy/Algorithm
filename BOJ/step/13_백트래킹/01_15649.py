# 백트래킹(Backtracking) 연습 1
# 중복 허용 x, 자릿값이 달라지면 다른 쌍임 - 순열

# 1. 백트래킹과 상태공간트리의 이해
import sys


def backtraking(level, n, m):
    # 공간 상태 깊이 체크
    if level == m:
        for i in range(m):
            print(seq[i], end=" ")
        print()
        return

    for i in range(1, n + 1):  # [1 ~ n] 범위
        if promising_check[i]:  # 중복 불허용 - 유망성(promising) 검사
            continue
        promising_check[i] = True  # 이 노드를 방문함
        seq[level] = i  # 방문 노드 기록 0->1 / 1->2 / 2->3
        backtraking(level + 1, n, m)  # 다음 레벨의 깊이에서 같은 탐색을 함.
        promising_check[i] = False  # 다녀옴 - 최대 깊이까지 다녀온 경우에 차례로 False


n, m = map(int, sys.stdin.readline().split())

promising_check = [False] * (n + 1)
seq = [0] * m

backtraking(0, n, m)


# # 2. 순열
# import sys
# from itertools import permutations

# n, m = map(int, sys.stdin.readline().split())

# numbers = [str(i) for i in range(1, n + 1)]  # join 사용하려고 str

# pair = permutations(numbers, m)  # permutation 객체 받음

# for nums in list(pair):
#     # print(nums)
#     print(" ".join(nums))
