import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    ps = input().rstrip()  # 괄호 문자열(Parenthesis String, PS)
    stack = []
    flag = True

    for c in ps:
        # 여는 괄호
        if c == "(":
            stack.append(c)
        elif c == ")":
            if not stack:
                flag = False
                break
            else:
                stack.pop()

    if flag == True and not stack:
        print("YES")
    else:
        print("NO")
