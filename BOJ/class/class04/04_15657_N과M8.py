import sys
input = sys.stdin.readline


def backtracking(idx, depth):
    if depth == m:
        print(" ".join(map(str, rst)))
        return

    for i in range(idx, n):
        rst.append(numbers[i])
        backtracking(i, depth + 1)
        rst.pop()


n, m = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort()
rst = []

backtracking(0, 0)


"""
04. 15657 N과 M (8) (Silver 3)
    - "15652 N과 M (4)"과 같은 문제 중복을 허용하며, 비내림차순 수열을 출력한다. 

    - 사전 순 출력을 위해 입력 값 수열을 소팅한다. 

    - 백트래킹의 기초를 공부할 수 있는 문제
"""
