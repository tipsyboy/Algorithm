# https://www.acmicpc.net/problem/7785

import sys

input = sys.stdin.readline

n = int(input())

working = set()
for _ in range(n):
    name, command = input().split()

    if command == "enter":
        working.add(name)
    else:
        working.remove(name)

working_list = list(working)
working_list.sort(reverse=True)
print("\n".join(working_list))
