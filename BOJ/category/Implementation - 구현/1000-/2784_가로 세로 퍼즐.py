# 2024.07.12 FRI
# https://www.acmicpc.net/problem/2784

import sys
from itertools import permutations

input = sys.stdin.readline


def is_possible(words_w, target, x):
    for i in range(3):
        if target[i] != words_w[i][x]:
            return False
    return True


words = []
ans = []
for _ in range(6):
    word = input().rstrip()
    words.append(word)

for words_combi in permutations(words, 6):
    flag = True
    for i in range(3):
        if not is_possible(words_combi[:3], words_combi[i + 3], i):
            flag = False
            break

    if flag:
        ans.append(words_combi)
        break

if not ans:
    print(0)
else:
    for i in range(3):
        print(ans[0][i])
