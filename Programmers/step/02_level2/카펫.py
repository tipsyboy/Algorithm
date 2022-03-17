def get_divisor(number):
    divisor = []

    for i in range(1, int(number ** 0.5) + 1):
        if number % i == 0:
            divisor.append(i)

    return divisor


def solution(brown, yellow):
    total_tile = brown + yellow

    divisor = get_divisor(yellow)

    for x in divisor:
        y = yellow // x

        if (x + 2) * (y + 2) == total_tile:
            return [y + 2, x + 2]


brown = 10
yellow = 2
print(solution(brown, yellow))
