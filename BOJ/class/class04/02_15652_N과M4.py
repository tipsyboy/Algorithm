import sys
input = sys.stdin.readline


def backtracking(idx, depth):
    if depth == m:
        print(" ".join(map(str, rst)))
        return

    for i in range(idx, n):
        rst.append(i + 1)
        backtracking(i, depth + 1)
        rst.pop()


n, m = map(int, input().split())
rst = []
backtracking(0, 0)


"""
02. 15652 N과 M (4) (Silver 4)
    - 중복을 허용하며(visited 사용 x), 비내림차순으로 수열을 고르는 문제이다.
      비 내림차순이라는 말은 선택한 수열이 오름차순을 갖게 되는 경우를 말하는데,
      이 때문에 idx로 이전에 선택했던 수 이상의 값만 선택해준다.(이전의 값은 선택해도됨 - 중복 가능)
      
    - 백트래킹의 기초를 공부할 수 있는 문제이다. 
"""
