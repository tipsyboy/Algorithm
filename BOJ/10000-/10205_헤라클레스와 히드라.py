# https://www.acmicpc.net/problem/10205

import sys

input = sys.stdin.readline

K = int(input())
for i in range(1, K + 1):
    h = int(input())
    commands = input().rstrip()
    for command in commands:
        if command == "c":
            h += 1
        else:
            h -= 1

    print("Data Set %d:" % i)
    print(h)
    if i != K:
        print()
