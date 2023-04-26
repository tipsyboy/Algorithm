# https://www.acmicpc.net/problem/11068

import sys

input = sys.stdin.readline
S = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/"


def convert_num_system(num: int, B: int) -> str:
    q, r = divmod(num, B)
    return convert_num_system(q, B) + S[r] if q else S[r]


def is_palindrome(num: str) -> bool:
    return True if num == num[::-1] else False


T = int(input())
for _ in range(T):
    num = int(input())
    flag = 0
    for base in range(2, 65):
        if is_palindrome(convert_num_system(num, base)):
            flag = 1
            break

    print(flag)


"""
11068. 회문인 수
    - B진법 변환 함수 작성 하기
    - 2~64 진수중에서 입력 받은 값이 팰린드롬인 경우를 전부 탐색한다.
"""