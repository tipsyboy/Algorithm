def solution(a, b):
    rst = 0

    for i in range(len(a)):
        rst += a[i] * b[i]

    return rst


def solution2(a, b):
    return sum([(va * vb) for va, vb in zip(a, b)])


print(solution([1, 2, 3, 4], [-3, -1, 0, 2]))
print(solution([-1, 0, 1], [1, 0, -1]))
