def solution(n):
    divisor = []

    for i in range(1, n//2 + 1):
        if n % i == 0:
            divisor.append(i)

    divisor.append(n)

    return sum(divisor)


print(solution(13))
