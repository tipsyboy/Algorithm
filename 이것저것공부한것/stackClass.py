# python으로 Stack 구현하기


class Stack:
    # 생성자
    def __init__(self):
        self.stack = []  # 객체를 생성할 때, list를 생성

    # 길이 반환
    def __len__(self):
        return len(self.stack)

    # ???
    def __str__(self):
        return str(self.stack[::1])

    # stack 구현 메소드
    # push, pop, clear, size, isempty, top(peek)
    def push(self, item):
        self.stack.append(item)

    # stack이 비어있는지 확인.
    def empty(self):
        if len(self.stack) == 0:
            return 1
        else:
            return 0

    def pop(self):
        # stack이 비어있는지 확인
        if self.empty():
            return -1
        else:
            return self.stack.pop()

    def size(self):
        return len(self.stack)

    def top(self):
        if self.empty():
            return -1
        else:
            return self.stack[-1]


a = Stack()
a.push(1)
print(a.pop())
