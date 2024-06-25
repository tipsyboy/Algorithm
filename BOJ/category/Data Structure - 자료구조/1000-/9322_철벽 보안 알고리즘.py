# https://www.acmicpc.net/problem/9322

import sys

input = sys.stdin.readline

TC = int(input())
answer = []
for _ in range(TC):
    n = int(input())
    public1 = list(input().split())
    public2 = list(input().split())
    cipher = list(input().split())

    p1_dict = {word: i for i, word in enumerate(public1)}
    to_go = {i: p1_dict[word] for i, word in enumerate(public2)}

    ans = [None] * n
    for i in range(n):
        ans[to_go[i]] = cipher[i]

    answer.append(" ".join(ans))

print(*answer, sep="\n")
