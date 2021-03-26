# # 1
# n = int(input())
# rst = 0

# for i in range(1, n+1):
#     x = list(map(int, str(i)))

#     if i + sum(x) == n:
#         rst = i
#         break

# print(rst)


###

n = int(input())

start = n - 9 * len(str(n))
end = n - 1 * len(str(n))
start = 1 if start < 1 else start
rst = 0

for i in range(start, end):
    x = list(map(int, str(i)))

    if i + sum(x) == n:
        rst = i
        break

print(rst)
