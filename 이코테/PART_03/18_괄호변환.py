# 올바른 괄호 문자열 검사
def is_proper_bracket(bracket):
    stack = []

    for b in bracket:
        if b == "(":
            stack.append(b)
        else:
            if stack:
                stack.pop()
            else:
                return False

    if stack:
        return False

    return True


# 균형 잡힌 괄호 문자열 찾기
def balenced_bracket(bracket):
    count = 0

    for i in range(len(bracket)):
        if bracket[i] == "(":
            count += 1
        else:
            count -= 1

        # count = 0이 되는 지점이 올바른 괄호 문자열은 아닐지라도, 균형은 잡혀있다.
        if count == 0:
            return i


# 메인
def solution(p):
    rst = ""
    if not p:
        return rst

    # u와 v - 균형 잡힌 괄호 문자열을 만든다
    idx = balenced_bracket(p)
    u = p[: idx + 1]
    v = p[idx + 1 :]

    # u가 올바른 문자열인 경우
    if is_proper_bracket(u):
        rst = u + solution(v)  # 올바른 문자열 u를 놔두고 v를 수행한다.
    else:
        temp = "("
        temp += solution(v)
        temp += ")"

        # u 의 처음 마지막 삭제후 뒤집기
        u = list(u[1:-1])

        for i in range(len(u)):
            if u[i] == "(":
                u[i] = ")"
            else:
                u[i] = "("

        rst = temp + "".join(u)

    return rst
