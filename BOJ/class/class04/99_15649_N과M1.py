import sys
from itertools import permutations
input = sys.stdin.readline


# 1) permutaition
def permutation(n, m):
    p = permutations(range(1, n + 1), m)

    for temp in p:
        print(" ".join(map(str, temp)))


# 2) backtracking
def backtracking(depth):
    if depth == m:
        print(" ".join(map(str, rst)))
        return

    for i in range(n):
        if not visited[i]:
            rst.append(i + 1)
            visited[i] = True
            backtracking(depth + 1)
            visited[i] = False
            rst.pop()


n, m = map(int, input().split())

# 1)
# permutation(n, m)

# 2)
rst = []
visited = [False] * n
backtracking(0)

"""
99. 15649 N과 M (1) (Silver 3)
    - 순열(permutations)
      itertools 라이브러리의 permutations로 구현되어 있다. 
    
    - 주어진 n개의 숫자중 m개의 수를 선택 후 놓는 문제이다. -> 즉, 순열과 정의가 같다. 
      문제에서 중복을 허용하지 않으며(visited로 중복관리)
      순서가 상관 있는 문제로 별도의 idx없이 depth와 visited로 문제를 해결한다. 

    - 백트래킹의 기초를 공부할 수 있는 문제
"""
