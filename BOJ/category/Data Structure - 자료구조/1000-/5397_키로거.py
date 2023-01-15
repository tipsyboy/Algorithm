# https://www.acmicpc.net/problem/5397
# 2022-08-13 Sat

import sys

input = sys.stdin.readline


def hack(init: str) -> str:
    left = []
    right = []

    for char in init:
        if char == "<":
            if left:
                right.append(left.pop())
        elif char == ">":
            if right:
                left.append(right.pop())
        elif char == "-":
            if left:
                left.pop()
        else:
            left.append(char)

    return "".join(left) + "".join(right[::-1])


TC = int(input())
for _ in range(TC):
    init = input().rstrip()
    print(hack(init))


"""
5397. 키로거
    - stack을 두개 정의해서 [커서 앞, 커서 뒤] 를 표현한다

    - 1406_에디터 와 같은 문제
"""