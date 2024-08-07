# 2024.08.02 FRI
# https://www.acmicpc.net/problem/1105

import sys

input = sys.stdin.readline


def palpal(L, R):
    l_len, r_len = len(L), len(R)

    # 1. 두 수의 자리수가 다름
    if l_len != r_len:
        return 0

    cnt = 0
    for i in range(l_len):
        if L[i] != R[i]:  # 2. 비교 자리수의 수가 다르면 항상 이후 뒷자리의 수가 8이 아니게 할 수 있음.
            break

        if L[i] == "8":  # 3. 자리수의 수가 같은데 8임 -> 8밖에 못옴.
            cnt += 1

    return cnt


L, R = input().split()
print(palpal(L, R))
