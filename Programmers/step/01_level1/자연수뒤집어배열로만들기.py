def solution(n):
    rst = list(map(int, str(n)))

    return rst[::-1]


print(solution(12345))
