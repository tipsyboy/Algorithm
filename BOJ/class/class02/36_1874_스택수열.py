# # 1) 첫 번째 코드 (통과)
# import sys
# input = sys.stdin.readline

# n = int(input())
# seq = [int(input()) for _ in range(n)]
# rst = []  # push/pop 저장 list result
# stack = []  # stack에 들어가 있는 수
# idx = 1  # 현재 뽑아야 하는 수

# while idx < n+1:
#     if not stack:
#         rst.append("+")
#         stack.append(idx)
#         idx += 1
#         continue

#     if stack[-1] == seq[0]:
#         rst.append("-")
#         stack.pop()
#         seq.pop(0)
#     else:
#         stack.append(idx)
#         rst.append("+")
#         idx += 1


# flag = True
# for _ in range(len(seq)):
#     if stack.pop() == seq[0]:
#         rst.append("-")
#         seq.pop(0)
#     else:
#         flag = False
#         break

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
