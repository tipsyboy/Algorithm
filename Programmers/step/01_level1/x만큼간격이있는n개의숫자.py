def solution(x, n):
    rst = [x]

    for i in range(n - 1):
        rst.append(rst[-1] + x)

    return rst


print(solution(2, 5))
print(solution(4, 3))
print(solution(-4, 2))
print(solution(4, 1))
