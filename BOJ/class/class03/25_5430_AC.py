import sys
from collections import deque
input = sys.stdin.readline


def AC(command, arr_length, arr):
    # 받은 arr의 길이보다 D가 많은 경우에 error를 발생 시킨다.
    if arr_length < command.count("D"):
        return "error"

    q = deque(arr)
    pointer = True  # 큐의 왼/오를 가리키는 포인터 - True가 왼쪽

    # command 처리
    for com in command:
        if com == "R":
            pointer = not pointer
        elif com == "D":
            if pointer:
                q.popleft()
            else:
                q.pop()

    # q = list(q) # list로 변환하지 않아도 reverse()와 join()을 사용할 수는 있더라
    if not pointer:
        q.reverse()

    return "[" + ",".join(q) + "]"


t = int(input())

for _ in range(t):
    command = input().rstrip()  # sys.stdin.line은 개행문자를 포함한다.
    arr_length = int(input())
    arr = input().rstrip()[1:-1].split(",")  # [~,~,~] 형태의 문자열 분리

    print(AC(command, arr_length, arr))
