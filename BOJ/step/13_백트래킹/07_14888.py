import sys

n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
operator = list(map(int, sys.stdin.readline().split()))  # [+, -, *, /]
rst = []


def operator_sort(level, result):
    if level == n:
        rst.append(result)
        return

    for i in range(4):
        # 유망 조건 - 넣을 수 있는 연산자 개수가 남아 있는가
        # 유망 조건이 단순해서 따로 함수 안만듬
        if operator[i] < 1:
            continue

        # 연산자 개수 하나 줄이고 맞는 함수를 호출
        operator[i] -= 1
        if i == 0:
            operator_sort(level+1, result + numbers[level])
        elif i == 1:
            operator_sort(level+1, result - numbers[level])
        elif i == 2:
            operator_sort(level+1, result * numbers[level])
        elif i == 3:  # 나눗셈은 방식이 다르므로
            if result < 0:
                result = ((result*-1) // numbers[level])*-1
                operator_sort(level+1, result)
            else:
                operator_sort(level+1, result // numbers[level])
        operator[i] += 1  # 돌아와서는 연산자 개수 늘려줌


operator_sort(1, numbers[0])
print(max(rst))
print(min(rst))
