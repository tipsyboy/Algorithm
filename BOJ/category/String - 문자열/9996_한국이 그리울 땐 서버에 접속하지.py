# https://www.acmicpc.net/problem/9996

"""
9996. 한국이 그리울 땐 서버에 접속하지
    
"""

import sys

input = sys.stdin.readline

N = int(input())
pattern = input().rstrip()

front = ""
for char in pattern:
    if char == "*":
        break
    front += char
back = ""
for char in pattern[::-1]:
    if char == "*":
        break
    back += char
back = back[::-1]

for _ in range(N):
    file_name = input().rstrip()

    if len(file_name) < len(front) + len(back):
        print("NE")
        continue

    if file_name[: len(front)] == front and file_name[-len(back) :] == back:
        print("DA")
    else:
        print("NE")
