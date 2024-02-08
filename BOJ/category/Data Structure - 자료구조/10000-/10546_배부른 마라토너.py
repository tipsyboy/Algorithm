# https://www.acmicpc.net/problem/10546

import sys

input = sys.stdin.readline

N = int(input())
participant = dict()
for _ in range(N):
    name = input().rstrip()
    participant[name] = participant.get(name, 0) + 1
for _ in range(N - 1):
    name = input().rstrip()
    participant[name] -= 1
    if participant[name] == 0:
        participant.pop(name)

print(list(participant.keys())[0])
