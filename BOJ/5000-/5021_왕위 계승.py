# 2024.11.16 SAT
# https://www.acmicpc.net/problem/5021

import sys
from collections import defaultdict, deque

input = sys.stdin.readline

N, M = map(int, input().split())
king = input().rstrip()
indegree = defaultdict(int)
info = defaultdict(list)
for _ in range(N):
    c, p1, p2 = input().split()

    indegree[c] = 2
    if p1 not in indegree:
        indegree[p1] = 0
    if p2 not in indegree:
        indegree[p2] = 0

    info[p1].append(c)
    info[p2].append(c)
candidates = [input().rstrip() for _ in range(M)]


q = deque()
for k, v in indegree.items():
    if v == 0:
        q.append(k)

blood = defaultdict(float)
blood[king] = 1
while q:
    parent = q.popleft()
    blood_parent = blood[parent]
    for child in info[parent]:
        blood[child] += blood_parent * 0.5
        indegree[child] -= 1
        if indegree[child] == 0:
            q.append(child)

ans = 0
name = None
for candidate in candidates:
    if blood[candidate] > ans:
        name = candidate
        ans = blood[candidate]
print(name)
