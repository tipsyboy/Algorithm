n = int(input())
numbers = list(map(int, input().split()))
operator = list(map(int, input().split()))

min_value = 1e9
max_value = -1e9


def dfs(rst, count):
    # 파이썬은 전역 변수 값이 함수 안에서 변경될 경우 global을 쓴다.
    global min_value, max_value

    # 연산자를 전부 사용한 경우
    if count == n - 1:
        min_value = min(min_value, rst)
        max_value = max(max_value, rst)

        return

    # 4개의 연산자 검사
    for i in range(4):
        if operator[i] > 0:  # 연산자가 있는 경우
            operator[i] -= 1  # 현재 연산자 하나 사용
            if i == 0:  # + 의 경우
                dfs(rst + numbers[count + 1], count + 1)
            elif i == 1:  # - 의 경우
                dfs(rst - numbers[count + 1], count + 1)
            elif i == 2:  # * 의 경우
                dfs(rst * numbers[count + 1], count + 1)
            elif i == 3:  # / 의 경우
                dfs(int(rst / numbers[count + 1]), count + 1)
            operator[i] += 1  # 돌아와서 연산자 다시 채움


dfs(numbers[0], 0)
print(max_value)
print(min_value)
