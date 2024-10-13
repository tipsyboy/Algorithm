# 2024.10.08 TUE
# https://www.acmicpc.net/problem/23294

import sys
from collections import deque

input = sys.stdin.readline


def backward(cur):
    if not back:
        return cur

    front.append(cur)
    return back.pop()


def frontward(cur):
    if not front:
        return cur
    back.append(cur)
    return front.pop()


def access(cur, nxt):
    global capacity

    for page in front:
        capacity -= CAP[page]
    front.clear()

    if cur != -1:
        back.append(cur)

    # 캐시 용량 추가
    capacity += CAP[nxt]

    # 최대 캐시 용량 초과
    while capacity > C and back:
        capacity -= CAP[back.popleft()]


def compress():
    global capacity

    rst = []
    for b in back:
        if not rst or b != rst[-1]:
            rst.append(b)
        else:
            capacity -= CAP[b]

    return deque(rst)


N, Q, C = map(int, input().split())
CAP = [0] + list(map(int, input().split()))
capacity = 0
back = deque()
front = []
cur = -1
for _ in range(Q):
    command = list(input().split())

    if command[0] == "B":
        cur = backward(cur)
    elif command[0] == "F":
        cur = frontward(cur)
    elif command[0] == "A":
        nxt = int(command[1])
        access(cur, nxt)
        cur = nxt
    elif command[0] == "C":
        back = compress()


print(cur)
print(*list(back)[::-1]) if back else print(-1)
print(*front[::-1]) if front else print(-1)
