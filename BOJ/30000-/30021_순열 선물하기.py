# 2024.09.17 TUE
# https://www.acmicpc.net/problem/30021

"""
30021. 순열 선물하기
    - (1<=N<=5000) 범위에서 [1, N]의 합 S가 소수가 되는 경우는 N=2일 때, S=3인 경우밖에 없다. 

    - 따라서, N=2인 경우는 성립하지 않고 이외의 값 N에 대해서 합이 3이 되지만 않게 나열하면 된다.
"""


import sys

input = sys.stdin.readline

N = int(input())
if N == 2:
    print("NO")
else:
    ans = list(range(1, N + 1))
    if N > 2:
        ans[1], ans[2] = ans[2], ans[1]
    print("YES")
    print(*ans)
