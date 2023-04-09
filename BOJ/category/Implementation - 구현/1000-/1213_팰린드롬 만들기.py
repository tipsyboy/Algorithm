# https://www.acmicpc.net/problem/1213

import sys

input = sys.stdin.readline


def is_palindrome(target: str) -> bool:
    return True if target == target[::-1] else False


S = input().rstrip()
alpha = [0] * 26
for char in S:
    alpha[ord(char) - 65] += 1

idx = 0
ans = ""
while True:
    flag = False

    for i in range(26):
        if alpha[i] // 2 > 0:
            idx += alpha[i] // 2
            ans += chr(i + 65) * (alpha[i] // 2)
            alpha[i] -= alpha[i] // 2 * 2
            flag = True
            break

    if not flag:
        break

back = ans[::-1]

for i in range(26):
    if alpha[i]:
        ans += chr(i + 65)

ans = ans + back
if is_palindrome(ans):
    print(ans)
else:
    print("I'm Sorry Hansoo")
