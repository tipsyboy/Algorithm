import sys

input = sys.stdin.readline

expression = input().rstrip()
rst = ""
stack = []  # 연산자 stack
priority = set(("*", "/"))  # 사칙연산 연산자 우선순위

for exp in expression:
    if exp.isalpha():  # 피연산자의 경우 바로 추가한다.
        rst += exp
    elif exp == "(":  # 여는 괄호 그냥 추가
        stack.append("(")
    elif exp == ")":  # 닫는 괄호의 경우 괄호 안의 수식들을 먼저 계산해야 하므로 여는 괄호를 만날때까지 pop한다.
        while stack and stack[-1] != "(":  # 당연히 stack은 비어있지 않아야한다.
            rst += stack.pop()
        stack.pop()  # 여는 괄호를 pop
    elif exp in priority:  # 연산자 우선순위가 +, -보다 높은 *, /의 경우
        while stack and stack[-1] in priority:  # 같은 연산자 우선순위의 연산자들을 계산한다.
            rst += stack.pop()
        stack.append(exp)  # 이후 자신을 추가
    else:  # 나머지 +, -의 경우
        # 자신보다 낮은 우선순위가 없기 때문에 괄호를 만나기 전까지는 전부 먼저 계산한다.
        while stack and stack[-1] != "(":
            rst += stack.pop()
        stack.append(exp)

# 남은 스택 처리
while stack:
    rst += stack.pop()

print(rst)


"""
44. 1918 후위 표기식 (Gold 3)
    - 중위 표기식을 -> 후위 표기식으로 바꾸기
      수식은 연산자와 괄호에 의해서 계산 순서가 바뀌기 때문에 이 점을 유의해서 표기식을 옮겨야 한다. 
      수식 expression을 입력 받았을 때, 각각의 exp가 가질 수 있는 문자는
      ["+", "-", "*", "/", "(", ")"] 6개와 피연산자들이다. 

      이때, 연산자의 우선순위를 갖는 것은 *, / 이고 괄호를 먼저 풀어주어야 하므로 서로 다른 처리가 필요하다. 
"""