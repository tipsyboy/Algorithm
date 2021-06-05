import sys
from itertools import combinations
input = sys.stdin.readline


# 1)
def backtracking(idx, depth):
    if depth == m:
        print(" ".join(map(str, rst)))
        return

    for i in range(idx, n):
        if not visited[i]:
            rst.append(i + 1)
            # visited[i] = True
            backtracking(i + 1, depth + 1)
            # visited[i] = False
            rst.pop()


# 2) combinations
def combi(n, m):
    c = combinations(range(1, n + 1), m)

    for temp in c:
        print(" ".join(map(str, temp)))


n, m = map(int, input().split())
rst = []
visited = [False] * n


# 1)
backtracking(0, 0)

# 2)
# combi(n, m)

"""
01. 15650 N과 M (2) (Silver 3)
    - 조합(Combination)
      itertools 라이브러리의 combinations로 구현되어 있다. 
    
    - 주어진 n개의 숫자중 m개의 수를 선택하는 문제이다. -> 즉, 조합과 정의가 같다. 
      문제에서 중복을 허용하지 않으며(visited로 중복관리) 순서에 상관없이 뽑기만 하는 문제이다.
      하지만, 하지만 오름차순으로 "출력"을 해야하므로 뽑기만 하는 조합의 정의와는 별개로 
      index를 활용해서 출력해준다. 

    - 백트래킹의 기초를 공부할 수 있는 문제
"""
