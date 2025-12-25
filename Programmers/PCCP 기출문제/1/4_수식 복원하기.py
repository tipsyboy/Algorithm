# https://school.programmers.co.kr/learn/courses/30/lessons/340210


def get_min_base(expression):
    min_base = -1
    for v in expression:
        if v.isnumeric():
            min_base = max(min_base, int(v))

    return min_base + 1


def convert_base(num, base):
    B = "0123456789"
    q, r = divmod(int(num), base)
    return convert_base(q, base) + B[r] if q else B[r]


def get_base_candidates(expression, base):
    expression_list = expression.split()
    left_val = convert_base(expression_list[0], base)
    right_val = convert_base(expression_list[2], base)
    result_val = convert_base(expression_list[4], base)
    operator = expression_list[1]

    if operator == "+" and left_val + right_val == result_val:
        return result_val
    if operator == "-" and left_val - right_val == result_val:
        return result_val

    return None


def calc(expression, base):
    expression_list = expression.split()
    left_val = convert_base(expression_list[0], base)
    right_val = convert_base(expression_list[2], base)
    operator = expression_list[1]

    if operator == "+":
        return convert_base(left_val + right_val, base)
    elif operator == "-":
        return convert_base(left_val - right_val, base)


def solution(expressions):
    min_base = 2
    for expression in expressions:
        min_base = max(min_base, get_min_base(expression))

    candidates = set(range(min_base, 10))
    for expression in expressions:
        if expression[-1] == "X":
            continue

        temp = set()
        for base in range(min_base, 10):
            rst = get_base_candidates(expression, base)
            if rst != None:
                temp.add(base)
        candidates = candidates & temp

    ans = []
    for expression in expressions:
        if expression[-1] != "X":
            continue
        rst = set()
        for base in list(candidates):
            rst.add(int(calc(expression, base)))
        if len(rst) == 1:
            ans.append(expression.replace("X", rst.pop()))
        else:
            ans.append(expression.replace("X", "?"))

    return ans


# print(solution(["14 + 3 = 17", "13 - 6 = X", "51 - 5 = 44"]))
# print(solution(["1 + 1 = 2", "1 + 3 = 4", "1 + 5 = X", "1 + 2 = X"]))
# print(solution(["10 - 2 = X", "30 + 31 = 101", "3 + 3 = X", "33 + 33 = X"]))
# print(solution(["2 - 1 = 1", "2 + 2 = X", "7 + 4 = X", "5 - 5 = X"]))
# print(solution(["2 - 1 = 1", "2 + 2 = X", "7 + 4 = X", "8 + 4 = X"]))
print(solution(["14 + 3 = X", "7 + 7 = X"]))  # 반례 테스트 케이스
