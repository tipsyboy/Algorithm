# 백트래킹(Backtracking) 연습 2
# 중복 허용 x, 오름차순 순서 - 순서 상관x - 조합

import sys


def back_prac(level):
    if level == m:  # 최대 깊이까지 탐색한 경우
        print(" ".join(map(str, result)))
        return

    # 하나의 가지의 경우의 수 [1 ~ n]
    for i in range(1, n + 1):
        if promising_check[i - 1]:
            continue

        result.append(i)  # 되는 경로 기록
        promising_check[i - 1] = True  # 방문 확인
        back_prac(level + 1)  # 방문노드로 이동해서 재탐색
        result.pop()  # 출력까지 하고 돌아왔으므로 마지막 경로를 지움.

        # 돌아와서 처리 - 현재 위치보다 하나 큰 트리까지만 False로 닫아주면됨.!
        for j in range(i, n):
            promising_check[j] = False


n, m = map(int, sys.stdin.readline().split())

# numbers = [i for i in range(1, n + 1)]
promising_check = [False] * n
result = []


back_prac(0)


# 2. 조합법
