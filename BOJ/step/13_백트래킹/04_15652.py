import sys


def back_prac(level):
    if level == m:
        print(" ".join(map(str, result)))
        return

    for i in range(1, n + 1):
        # 유망성 검사 -
        if promising_check[i - 1]:
            continue

        result.append(i)  # 경로 추가
        back_prac(level + 1)  # 중복이 허용되니까 호출
        promising_check[i - 1] = True  # 방문확인
        result.pop()

        # 돌아온 현재 레벨 트리에서는 그대로다.
        for j in range(i, n):
            promising_check[j] = False


n, m = map(int, sys.stdin.readline().split())

promising_check = [False] * n  # 유망성 검사
result = []


back_prac(0)
