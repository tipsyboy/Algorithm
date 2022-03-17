# # 1. 틀렸음
# def solution(number, k):
#     pick_num = len(number) - k  # 남은 뽑아야 하는 수

#     idx = 0
#     rst = ""

#     while idx < len(number):
#         max_val = -1
#         for i in range(idx, len(number)):
#             if len(number) - i < pick_num:
#                 break

#             if int(max_val) < int(number[i]):
#                 max_val = number[i]
#                 temp = i  # temp idx

#         pick_num -= 1
#         rst += max_val
#         idx = temp + 1

#     return rst


def solution(number, k):
    stack = []

    for num in number:
        while k and stack and stack[-1] < num:
            stack.pop()
            k -= 1

        stack.append(num)

    return "".join(stack[: len(stack) - k]) # 만들어진 stack에서 남은 k만큼 날려줌
    """
    이 부분에서 number-k로 했는데 플머스는 통과함;;
    반례
    6 4
    198794
    답 99
    """



print(solution("4177252841", 1))
