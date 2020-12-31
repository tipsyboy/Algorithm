def solution(a, b):
    AB = a * b

    # get gcd
    while True:
        remainder = a % b

        if remainder == 0:
            gcd = b
            break

        a, b = b, remainder

    # get lcm
    lcm = int(AB / gcd)

    return [gcd, lcm]


print(solution(3, 12))
print(solution(2, 5))
