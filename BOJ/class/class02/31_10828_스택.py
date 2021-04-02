import sys
input = sys.stdin.readline


def push(item):
    stack.append(item)


def empty():
    if stack:  # 안 비어 있는 경우
        return 0

    return 1  # 비어 있는 경우


def pop():
    if empty():
        return -1

    return stack.pop()


def size():
    return len(stack)


def top():
    if empty():
        return -1

    return stack[-1]


#
n = int(input())
stack = []

for _ in range(n):
    input_command = input().rstrip().split()
    command = input_command[0]

    if command == "push":
        push(int(input_command[1]))
    elif command == "empty":
        print(empty())
    elif command == "pop":
        print(pop())
    elif command == "size":
        print(size())
    elif command == "top":
        print(top())
