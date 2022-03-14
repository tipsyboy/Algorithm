import sys

input = sys.stdin.readline


def solution1():
    n = int(input())
    arr = list(map(int, input().split()))

    stack = []
    rst = []

    for _ in range(n):
        x = arr.pop()

        if stack:
            if stack[-1] > x:
                rst.append(stack[-1])
                # stack.append(x)
            else:
                while stack and stack[-1] <= x:
                    stack.pop()

                if stack:
                    rst.append(stack[-1])
                    # stack.append(x)
                else:
                    rst.append(-1)
                    # stack.append(x)
        else:
            rst.append(-1)
            # stack.append(x)
        stack.append(x)

    return rst[::-1]


def solution2():
    n = int(input())
    arr = []


print(*solution1())
print(solution2())