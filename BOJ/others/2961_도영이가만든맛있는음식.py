import sys
from itertools import combinations

input = sys.stdin.readline
INF = int(1e9)


def solution1():
    n = int(input())
    food = []
    rst = INF

    for _ in range(n):
        a, b = map(int, input().split())
        food.append((a, b))  # 신, 쓴

    combination = []
    for i in range(1, n + 1):
        combination.append(combinations(food, i))

    for combi in combination:
        for each in combi:
            sour, bitter = 1, 0
            for com in each:
                sour *= com[0]
                bitter += com[1]

            rst = min(rst, abs(sour - bitter))

    return rst


def dfs(n, bit_arr, depth, food):
    global rst
    if depth == n:
        if sum(bit_arr) == 0:
            return

        sour, bitter = 1, 0
        for i in range(len(bit_arr)):
            if bit_arr[i] == 1:
                sour *= food[i][0]
                bitter += food[i][1]

        rst = min(rst, abs(sour - bitter))
        return

    for i in range(2):
        temp = bit_arr[depth]
        bit_arr[depth] = i
        dfs(n, bit_arr, depth + 1, food)
        bit_arr[depth] = temp


def solution2():
    global rst

    n = int(input())
    food = []
    for _ in range(n):
        a, b = map(int, input().split())
        food.append((a, b))

    bit_arr = [0] * n
    dfs(n, bit_arr, 0, food)


rst = INF
# print(solution())
solution2()
print(rst)
