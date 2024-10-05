# 2024.10.01 TUE
# https://www.acmicpc.net/problem/31799

import sys

input = sys.stdin.readline

N = int(input())
S = input().rstrip()


def convert_grade(n, prev, grade):
    if grade in {"C+", "C0", "C-"}:
        return "B"

    if grade in {"B0", "B-"}:
        if n == 0 or prev in {"C+", "C0", "C-"}:
            return "D"
        return "B"

    if grade in {"A-", "B+"}:
        if n == 0 or prev in {"B0", "B-", "C+", "C0", "C-"}:
            return "P"
        return "D"

    if grade == "A0":
        if n == 0 or prev in {"A-", "B+", "B0", "B-", "C+", "C0", "C-"}:
            return "E"
        return "P"

    return "E"


grades = []
for i in range(len(S)):
    if S[i] in {"+", "-", "0"}:
        continue

    G = S[i]
    if i != len(S) - 1 and S[i + 1] not in {"A", "B", "C"}:
        G += S[i + 1]

    if len(G) < 2:
        G += "0"

    grades.append(G)

ans = []
for i in range(N):
    prev = grades[i - 1] if i > 0 else None
    ans.append(convert_grade(i, prev, grades[i]))
print("".join(ans))
