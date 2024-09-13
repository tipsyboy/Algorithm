# 2024.09.06 FRI
# https://www.acmicpc.net/problem/25542


import sys

input = sys.stdin.readline


def diff(target, ref):
    c = 1
    for i in range(L):
        if target[i] != ref[i]:
            if c:
                c -= 1
            else:
                return False

    return True


N, L = map(int, input().split())
store_names = [input().rstrip() for _ in range(N)]

cand_alpha = [set() for _ in range(L)]
for i in range(N):
    for j in range(L):
        cand_alpha[j].add(store_names[i][j])

candidates = set()
target = list(store_names[0])
for i in range(L):
    for alpha in list(cand_alpha[i]):
        target[i], alpha = alpha, target[i]
        candidates.add("".join(target))
        target[i], alpha = alpha, target[i]

ans = []
for cand in list(candidates):
    diff_one = True
    for i in range(N):
        if not diff(cand, store_names[i]):
            diff_one = False
            break

    if diff_one:
        ans.append(cand)

if ans:
    print(ans[0])
else:
    print("CALL FRIEND")
