# https://www.acmicpc.net/problem/12018

"""
12018. Yonsei TOTO.py
    1. 1~36의 마일리지 부여 / 같은 마일리지인 경우 우선순위를 가짐
    2. L(수강 인원) 안에만 들면됨
    3. 가진 마일리지가 한정적이며, 특정 과목을 포기하고 두 과목 이상 들을 수 있는 경우가 있고, 
       과목 상관 없이 최대 신청 과목을 가져가는게 목표이므로 정렬 후 그리디하게 해결
"""


import sys

input = sys.stdin.readline

n, m = map(int, input().split())
need = []
for _ in range(n):
    P, L = map(int, input().split())
    points = list(map(int, input().split()))

    if L > P:
        need.append(1)
        continue

    points.sort(reverse=True)
    need.append(points[L - 1])


need.sort()
ans = 0
for po in need:
    if po > m:
        break

    m -= po
    ans += 1
print(ans)