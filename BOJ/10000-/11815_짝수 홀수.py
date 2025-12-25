# https://www.acmicpc.net/problem/11815

"""
11815. 짝수? 홀수?
    1. 약수의 개수는 수 x가 제곱수인 경우 홀수 개, 제곱수가 아닌 경우 짝수 개를 갖는다.
    2. but, 부동소수점 오차를 고려해서 해결해야함..    
"""


import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
ans = []
for X in nums:
    if int(X ** 0.5) ** 2 == X:
        ans.append(1)
    else:
        ans.append(0)

print(" ".join(map(str, ans)))