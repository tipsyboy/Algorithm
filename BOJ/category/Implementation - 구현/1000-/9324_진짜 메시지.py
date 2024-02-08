# https://www.acmicpc.net/problem/9324

import sys

input = sys.stdin.readline

TC = int(input())
for _ in range(TC):
    M = input().rstrip()

    alpha = [0] * 26
    ans = "OK"

    i = 0
    while i < len(M):
        char_n = ord(M[i]) - 65
        alpha[char_n] += 1

        if alpha[char_n] == 3:
            if i + 1 >= len(M) or M[i + 1] != M[i]:
                ans = "FAKE"
                break

            alpha[char_n] = 0
            i += 1

        i += 1

    print(ans)
