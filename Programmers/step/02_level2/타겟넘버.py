def dfs(numbers, depth, sum_, target):
    if depth == len(numbers):
        if sum_ == target:
            return 1
        return 0

    p = dfs(numbers, depth + 1, sum_ + numbers[depth], target)
    m = dfs(numbers, depth + 1, sum_ - numbers[depth], target)

    return p + m


def solution(numbers, target):
    return dfs(numbers, 0, 0, target)


numbers = [1, 1, 1, 1, 1]
target = 3
print(solution(numbers, target))
