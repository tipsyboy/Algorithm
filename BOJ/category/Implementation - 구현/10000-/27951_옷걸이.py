# 2024.08.27 TUE
# https://www.acmicpc.net/problem/27951

import sys

input = sys.stdin.readline


def sol(A, U, D):
    X = U - A.count(1)

    if X < 0:
        return []

    ans = []
    for i in range(N):
        if A[i] == 1:
            if not U:
                return []
            U -= 1
            ans.append("U")
        elif A[i] == 2:
            if not D:
                return []

            D -= 1
            ans.append("D")
        else:
            if X:
                U -= 1
                X -= 1
                ans.append("U")
            else:
                D -= 1
                ans.append("D")

    return ans


N = int(input())
A = list(map(int, input().split()))
U, D = map(int, input().split())

ans = sol(A, U, D)
if ans:
    print("YES")
    print("".join(ans))
else:
    print("NO")
