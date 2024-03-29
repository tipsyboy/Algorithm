# https://www.acmicpc.net/problem/1380

import sys

input = sys.stdin.readline

scenario = 1
while True:
    n = int(input())
    if n == 0:
        break

    names = []
    for i in range(n):
        name = input().rstrip()
        names.append(name)

    is_back = [0] * n
    for _ in range(2 * n - 1):
        num, _ = input().split()
        is_back[int(num) - 1] += 1

    print(f"{scenario} {names[is_back.index(1)]}")
    scenario += 1
