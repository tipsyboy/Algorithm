# S2 1541 잃어버린 괄호
import sys
input = sys.stdin.readline

exp = input().split("-")
rst = 0

for i in range(len(exp)):
    temp = exp[i].split("+")

    if i == 0:
        for t in temp:
            rst += int(t)
    else:
        for t in temp:
            rst -= int(t)


print(rst)
