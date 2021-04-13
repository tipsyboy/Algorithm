import sys

input = sys.stdin.readline

# # 1) set 자료형 이용
# n, m = map(int, input().split())
# no_hear = set()
# count = 0
# rst = []

# for _ in range(n):
#     no_hear.add(input().strip())

# for _ in range(m):
#     temp = input().strip()

#     if temp in no_hear:
#         count += 1
#         rst.append(temp)

# print(count)
# print("\n".join(sorted(rst)))


# 2) binary search 이용
def binary_search(arr, target, start, end):
    if start > end:
        return False

    mid = (start + end) // 2

    if arr[mid] == target:
        return True
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, end)


n, m = map(int, input().split())
no_hear = sorted([input().strip() for _ in range(n)])
no_see = sorted([input().strip() for _ in range(m)])
rst = []

for target in no_hear:
    if binary_search(no_see, target, 0, len(no_see) - 1):
        rst.append(target)

print(len(rst))
print("\n".join(sorted(rst)))
