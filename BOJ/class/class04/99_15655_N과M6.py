import sys
input = sys.stdin.readline


def backtracking(idx, depth):
    if depth == m:
        print(" ".join(map(str, rst)))
        return

    for i in range(idx, n):
        if not visited[i]:
            rst.append(numbers[i])
            # visited[i] = True
            backtracking(i + 1, depth + 1)
            # visited[i] = False
            rst.pop()


n, m = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort()
rst = []
visited = [False] * n

backtracking(0, 0)

"""
99. 15655 N과 M (6) (Silver 3)
    - "15650 N과 M (2)"과 같은 문제 뽑기만 한다. 

    - 사전순 출력을 위해서 입력 값 수열을 소팅한다. 
    
    - 백트래킹의 기초를 공부할 수 있는 문제
"""
