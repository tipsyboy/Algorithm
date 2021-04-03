import sys
input = sys.stdin.readline


def push(item):
    que.append(item)


def empty():
    if que:
        return 0

    return 1


def pop():
    if empty():
        return -1

    return que.pop(0)


def size():
    return len(que)


def front():
    if empty():
        return -1

    return que[0]


def back():
    if empty():
        return -1

    return que[-1]


n = int(input())
que = []

for _ in range(n):
    input_command = input().split()
    command = input_command[0]

    if command == "push":
        push(int(input_command[1]))
    elif command == "pop":
        print(pop())
    elif command == "size":
        print(size())
    elif command == "empty":
        print(empty())
    elif command == "front":
        print(front())
    elif command == "back":
        print(back())
