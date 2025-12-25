# https://www.acmicpc.net/problem/6064
# 2022-08-11 Thu

import sys

input = sys.stdin.readline


def gcd(a: int, b: int) -> int:
    while b:
        r = a % b
        a = b
        b = r

    return a


def lcm(a: int, b: int) -> int:
    return a * b // gcd(a, b)


def solution(M: int, N: int, x: int, y: int) -> int:
    if x == M:  # 4)
        x = 0
    if y == N:
        y = 0

    lcmMN = lcm(M, N)
    for i in range(x, lcmMN + 1, M):
        if i == 0:  # 5)
            continue
        if i % N == y:
            return i

    return -1


TC = int(input())
for _ in range(TC):
    M, N, x, y = map(int, input().split())
    print(solution(M, N, x, y))

"""
6064. 카잉 달력
    - 1) 문제를 다시 생각하면 M으로 나눈 나머지가 x and N으로 나눈 나머지가 y인 idx를 구하라는 말이 된다. 
    
    - 2) 문제의 달력은 <M:N>까지 이므로 마지막번째 max(idx)는 lcm(M, N)이 된다. 
      왜냐하면 idx는 M으로도 N으로도 나누어 떨어져야 하기 때문이다. 

    - 3) 유효하지 않은 쿼리 <x:y>가 입력되는 경우가 있다. 

    - 4) 1)을 생각하고 문제 풀이를 진행하면 되지만 달력은 <1:1>부터 시작한다. 
      but, 나눈 나머지들을 생각 했을 때, {0, 1, 2... M-1}의 꼴이므로 x == M인 경우를 찾을 수 없다.
      따라서, 23번째 줄처럼 예외처리를 동반한다. (y==N인 경우에도 마찬가지다.)

    - 5) 이제 idx <- [1..lcm(M, N)]의 범위에서 idx%M == x and idx%N == y인 idx를 찾으면 되나 
      시간 복잡도를 따져 봤을때, O(lcm(M, N))이 되고 M, N <= 40000 이므로 1s에는 힘들것이다. 
      
      때문에 조금 더 효율적인 방법을 찾아야 하는데, 
      idx%M == x 인 idx만을 탐색하면서 idx%N==y에 대해서 찾아주면 탐색범위가 상당히 줄어들 것이다. 
      (idx%M == x 인 경우는 idx <- (x to lcm(M, N), +=M)으로 진행하면 idx%M == x은 항상 성립)
      
      이때, i==0 인 경우를 건너뛰는 이유는 x==M인 경우 x=0으로 예외 처리를 해줬기 때문에 
      x == M인 경우를 찾기위해서 이다. 
"""