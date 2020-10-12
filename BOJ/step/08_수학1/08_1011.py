import sys
from math import sqrt  # math class module

T = int(sys.stdin.readline())  # 테스트 케이스 T

for i in range(T):
    x, y = map(int, sys.stdin.readline().split())  # x: 출발지점, y:도착지점
    dist = y - x  # distance 거리

    n = int(sqrt(dist))  # 제곱수 구하기

    if n*n == dist:
        print(2*n-1)
    elif n*n < dist <= n*n + n:
        print(2*n)
    else:
        print(2*n+1)

"""
실제로 dist == 20번째 정도까지 하면서 추론


제곱수를 기점(제곱수를 기점으로 n값만큼 늘어나고 줄어들면서 횟수증가/감소)으로 두 분류로 나눠서 도착 점프횟수가 증가함
위는 그것을 식으로 나타낸 것

"""
