# 2025.02.26 WED
# https://www.acmicpc.net/problem/2503

import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input())
candidate_nums = permutations(range(1, 10), 3)

for _ in range(N):
    query, s, b = map(int, input().split())
    query = str(query)
    temp = []
    for candidate in candidate_nums:
        candidate = list(map(str, candidate))
        qs, qb = 0, 0
        for i in range(3):
            if candidate[i] == query[i]:
                qs += 1
            elif candidate[i] in query:
                qb += 1

        if qs == s and qb == b:
            temp.append(candidate)

    candidate_nums = temp

print(len(candidate_nums))
