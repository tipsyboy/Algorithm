# # 1) queue
# n, k = map(int, input().split())
# people = [x for x in range(1, n+1)]

# rst = []

# while people:
#     for _ in range(k-1):
#         item = people.pop(0)
#         people.append(item)

#     rst.append(people.pop(0))

# print("<", end="")
# for i in range(n-1):
#     print(f"{rst[i]}, ", end="")
# print(f"{rst[-1]}>")


# 2) indexing
n, k = map(int, input().split())
people = [x for x in range(1, n+1)]

idx = 0
rst = []

while people:
    idx += k

    if idx > len(people):
        idx = idx % len(people)
        if idx == 0:
            idx += len(people)

    idx -= 1
    rst.append(people.pop(idx))

print(rst)
