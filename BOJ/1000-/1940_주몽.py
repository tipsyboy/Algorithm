import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
arr = list(map(int, input().split()))
arr.sort()

lo, hi = 0, N - 1
ans = 0
while lo < hi:
    temp = arr[lo] + arr[hi]
    if temp == M:
        lo += 1
        hi -= 1
        ans += 1
    elif temp > M:
        hi -= 1
    else:
        lo += 1

print(ans)


"""
1940. 주몽
    - 간단한 투 포인터
"""