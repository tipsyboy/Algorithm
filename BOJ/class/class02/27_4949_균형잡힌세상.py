import sys
input = sys.stdin.readline

while True:
    input_str = input().rstrip()
    stack = []
    flag = True

    if input_str == ".":
        break

    # 문자열 검사
    for s in input_str:
        # 여는 괄호인 경우
        if s == "(" or s == "[":
            stack.append(s)
        # 닫는 괄호인 경우
        elif s == ")":
            if not stack or stack.pop() != "(":
                flag = False
                break
        elif s == "]":
            if not stack or stack.pop() != "[":
                flag = False
                break

    # 결과
    # 여는 괄호와 닫는 괄호의 매칭이 다 되어있고, and STACK도 비어 있어야한다.
    if flag == True and not stack:
        print("yes")
    else:
        print("no")
