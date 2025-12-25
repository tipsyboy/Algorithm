# Mar 25, 2025 Tue
# https://www.acmicpc.net/problem/25631

import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
A = Counter(map(int, input().split()))
print(A.most_common()[0][1])
