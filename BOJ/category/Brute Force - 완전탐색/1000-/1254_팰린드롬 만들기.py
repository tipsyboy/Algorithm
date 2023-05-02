# https://www.acmicpc.net/problem/1254

import sys

input = sys.stdin.readline

# 1
def is_palindrome(S: str, bword: str) -> bool:
    temp = S + bword
    return temp == temp[::-1]


S = input().rstrip()
for i in range(len(S) + 1):
    if is_palindrome(S, S[:i][::-1]):
        print(len(S) + i)
        break


# # 2
# S = input().rstrip()
# for i in range(len(S)):
#     if S[i:] == S[i:][::-1]:
#         print(i + len(S))
#         break
