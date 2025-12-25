# 2024.08.20 TUE
# https://www.acmicpc.net/problem/13171


import sys

input = sys.stdin.readline
DIV = 1_000_000_007


def sol1(A, X):
    digit = A % DIV
    ans = 1
    while X:
        if X & 1:
            ans = (ans * digit) % DIV

        X >>= 1
        digit = (digit**2) % DIV

    return ans % DIV


def sol2(A, X):
    def power(a, x):
        if x == 0:
            return 1

        half = power(a, x // 2) % DIV
        if x & 1:
            return (half * half * a) % DIV
        else:
            return (half * half) % DIV

    return power(A, X)


A = int(input())
X = int(input())

print(sol1(A, X))
print(sol2(A, X))
