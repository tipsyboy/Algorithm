import sys
input = sys.stdin.readline


def backtracking(depth):
    if depth == m:
        print(" ".join(map(str, rst)))
        return

    for i in range(n):
        if not visited[i]:
            rst.append(numbers[i])
            visited[i] = True
            backtracking(depth + 1)
            visited[i] = False
            rst.pop()


#
n, m = map(int, input().split())
numbers = list(map(int, input().split()))
visited = [False] * n

numbers.sort()
rst = []

backtracking(0)


"""
03. 15654 N과 M (5) (Silver 3)
    - "15649 N과 M (1)"과 똑같은 문제 그냥 후보 수열이 입력 값으로 변경된 문제일 뿐이다. 

    - 사전 증가 순서로 출력하기 위해서 받은 수열 값을 소팅한다. 

    - 백트래킹의 기초를 공부할 수 있는 문제
"""
