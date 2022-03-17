from itertools import permutations


def is_prime(x):
    if x < 2:
        return False

    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False

    return True


def get_numbers(numbers):
    numbers = list(map(str, numbers))
    rst = set()
    for i in range(1, len(numbers) + 1):
        for temp in permutations(numbers, i):
            rst.add(int("".join(temp)))

    return list(rst)


def solution(numbers):
    nums = get_numbers(numbers)

    count = 0
    for num in nums:
        if is_prime(num):
            count += 1

    return count


numbers = "17"
print(solution(numbers))
