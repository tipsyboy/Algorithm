import sys
input = sys.stdin.readline


def push_front(item):
    deque.insert(0, item)


def push_back(item):
    deque.append(item)


def pop_front():
    if empty():
        return -1

    return deque.pop(0)


def pop_back():
    if empty():
        return -1

    return deque.pop()


def size():
    return len(deque)


def empty():
    if deque:
        return 0

    return 1


def front():
    if empty():
        return -1

    return deque[0]


def back():
    if empty():
        return -1

    return deque[-1]


n = int(input())
deque = []

for _ in range(n):
    input_command = input().split()
    command = input_command[0]

    if command == "push_front":
        push_front(input_command[1])
    elif command == "push_back":
        push_back(input_command[1])
    elif command == "pop_front":
        print(pop_front())
    elif command == "pop_back":
        print(pop_back())
    elif command == "size":
        print(size())
    elif command == "empty":
        print(empty())
    elif command == "front":
        print(front())
    elif command == "back":
        print(back())
