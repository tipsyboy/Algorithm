# 1)
# import sys

# input = sys.stdin.readline

# n = int(input())
# seq = []
# for _ in range(n):
#     seq.append(int(input()))

# rst = ""
# stack = []
# now = 1  # 현재 번호
# idx = 0  # seq index

# while now < n + 1:
#     if not stack:
#         stack.append(now)
#         now += 1
#         rst += "+"
#         continue

#     if stack[-1] != seq[idx]:
#         stack.append(now)
#         rst += "+"
#         now += 1
#     else:
#         stack.pop()
#         rst += "-"
#         idx += 1

# # 남은 stack 처리
# flag = True
# for i in range(idx, n):
#     if stack.pop() == seq[i]:
#         rst += "-"
#     else:
#         flag = False

# if flag:
#     print("\n".join(rst))
# else:
#     print("NO")

# 2)
import sys

input = sys.stdin.readline

n = int(input())
idx = 1  # input number
rst = ""  # result
stack = []
flag = True

for _ in range(n):
    number = int(input())

    while idx <= number:
        stack.append(idx)
        idx += 1
        rst += "+"

    if stack.pop() == number:
        rst += "-"
    else:
        flag = False
        break

if flag:
    print("\n".join(rst))
else:
    print("NO")
