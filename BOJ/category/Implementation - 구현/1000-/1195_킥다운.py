# 2024.08.01 THU
# https://www.acmicpc.net/problem/1195

import sys

input = sys.stdin.readline

A = input().rstrip()
B = input().rstrip()
if len(A) < len(B):
    A, B = B, A

a_len, b_len = len(A), len(B)
ans = a_len + b_len
for a_start in range(-b_len + 1, a_len):
    a_idx = a_start - 1

    flag = True
    for b_idx in range(b_len):
        a_idx += 1
        if a_idx < 0 or a_idx >= a_len:
            continue

        if A[a_idx] == B[b_idx] == "2":  # 맞물리지 않는다.
            flag = False
            break

    if flag:
        if a_start < 0:
            ans = min(ans, a_len - a_start)
        elif a_start > a_len - b_len:
            ans = min(ans, b_len + a_start)  # al + bl - (al - as)
        else:
            ans = a_len
            break
print(ans)
