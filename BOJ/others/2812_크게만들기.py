import sys

input = sys.stdin.readline


def solution(number, k):
    stack = []

    for num in number:
        while k and stack and stack[-1] < num:
            stack.pop()
            k -= 1

        stack.append(num)

    return "".join(stack[: len(stack) - k])  # 만들어진 stack에서 남은 k만큼 날려줌


n, k = map(int, input().split())
number = input().rstrip()

print(solution(number, k))


"""

"""