# 2024.08.26 MON
# https://www.acmicpc.net/problem/12174

import sys

input = sys.stdin.readline

T = int(input())
for case in range(T):
    N = int(input())
    binary = input().rstrip()
    sentence = ""
    for i in range(N):
        target = binary[i * 8 : (i + 1) * 8]
        target = target.replace("O", "0")
        target = target.replace("I", "1")

        print(target, type)
        sentence += chr(int(target, 2))
    print(f"Case #{case+1}: {sentence}")
