# https://www.acmicpc.net/problem/1083

"""
    28일에 복습임
"""

import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
S = int(input())

p = 0
while S and p < N:
    maxv = max(A[p : p + S + 1])
    idx = A.index(maxv)

    S -= idx - p
    for i in range(idx, p, -1):
        A[i] = A[i - 1]

    A[p] = maxv
    p += 1
print(*A)


"""
1083. 소트
    - 높은 수가 높은 자리에 위치 해야하는데, 연속된 수만 교환할 수 있으므로 처음에는 무지성 스왑하면 되는줄
      틀렸음

    - 남은 교환 S만큼에서 위치가 결정된 수 이후의 수에서 가장 큰 수를 가져온다.
"""