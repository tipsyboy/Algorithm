

def factorial(N):
    if N <= 1:  # 범위가 0보다 크거나 같은 범위
        return 1

    return N * factorial(N-1)


N = int(input())
print(factorial(N))
