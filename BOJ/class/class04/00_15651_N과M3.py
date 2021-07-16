import sys
input = sys.stdin.readline


def backtracking(depth):
    if depth == m:
        print(" ".join(map(str, rst)))
        return

    for i in range(n):
        rst.append(i + 1)
        backtracking(depth + 1)
        rst.pop()


n, m = map(int, input().split())
rst = []
backtracking(0)


"""
99. 15651 N과 M (3) (Silver 3)
    - 백트래킹 문제로 중복 순열에 관한 문제이다. 
      수를 뽑아서 놓는 문제로 숫자를 중복으로 뽑아도 된다는 점에서 중복순열 문제이다. 
      따라서 순서가 상관 있으며(순서가 다르면 다른 수열), 중복을 허용하므로
      visited나 idx 등 다른 장치 없이 재귀로 찾아주면 된다. 

    - 백트래킹의 기초를 공부할 수 있는 문제
"""
