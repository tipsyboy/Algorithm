# # 1)
# import sys
# input = sys.stdin.readline


# def cut_trees(trees, m, start, end):
#     global result
#     if end < start:
#         return

#     total = 0
#     mid = (start+end) // 2

#     for tree in trees:
#         if tree > mid:
#             total += tree - mid

#     if total < m:
#         cut_trees(trees, m, start, mid-1)
#     else:
#         result = mid
#         cut_trees(trees, m, mid+1, end)


# n, m = map(int, input().split())  # 나무 수, 필요 길이
# trees = list(map(int, input().split()))
# result = 0

# cut_trees(trees, m, 0, max(trees))
# print(result)


# # 2) 시간초과... 왜? 위에껀 되고 이건 안되지..?
# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# trees = list(map(int, input().split()))

# result = 0
# start, end = 1, max(trees)

# while start <= end:
#     mid = (start + end) // 2
#     total = 0

#     for tree in trees:
#         if tree > mid:
#             total += tree - mid
#             if total >= m:
#                 break

#     if total < m:
#         end = mid - 1
#     else:
#         result = mid
#         start = mid + 1

# print(result)


# 3) Counter 사용
from collections import Counter
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = Counter(map(int, input().split()))
start, end = 0, max(trees)
result = 0

while start <= end:
    total = 0
    mid = (start+end) // 2

    for tree, cnt in trees.items():
        if tree > mid:
            total += (tree - mid) * cnt

    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)
