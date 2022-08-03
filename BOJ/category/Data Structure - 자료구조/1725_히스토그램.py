import sys

input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

stk = []
ans = [0] * N
for i in range(N):
    while stk and arr[stk[-1]] > arr[i]:
        x = stk.pop()
        height = arr[x]
        width = i if not stk else i - 1 - stk[-1]
        ans[x] = height * width
    stk.append(i)

while stk:
    x = stk.pop()
    height = arr[x]
    width = N if not stk else N - 1 - stk[-1]
    ans[x] = height * width

print(max(ans))


"""
1725. 히스토그램
    - 웰 노운
"""