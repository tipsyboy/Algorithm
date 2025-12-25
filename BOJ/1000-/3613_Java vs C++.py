# https://www.acmicpc.net/problem/3613

import sys

input = sys.stdin.readline


def is_cpp(target: str) -> bool:
    if target[0] == "_" or target[-1] == "_":
        return False

    if "__" in target:
        return False

    for char in target:
        if char == "_":
            continue

        if char.isupper() or not char.isalpha():
            return False

    return True


def is_java(target: str) -> bool:
    if target[0].isupper():
        return False

    if "_" in target:
        return False

    return True


def cpp_to_java(target: str) -> str:
    ans = target[0]
    for i in range(1, len(target)):
        if target[i] == "_":
            continue

        if target[i - 1] == "_":
            ans += target[i].upper()
        else:
            ans += target[i]

    return ans


def java_to_cpp(target: str) -> str:
    ans = ""
    for char in target:
        if char.isupper():
            ans += "_" + char.lower()
        else:
            ans += char

    return ans


S = input().rstrip()
c = is_cpp(S)
j = is_java(S)

if c:
    print(cpp_to_java(S))
elif j:
    print(java_to_cpp(S))
else:
    print("Error!")