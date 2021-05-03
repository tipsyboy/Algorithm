# 1. Combination의 정의를 이용한 방법
def factorial(n):
    rst = 1

    for i in range(1, n + 1):
        rst *= i

    return rst


def bino_coef_factorial(n, r):
    return factorial(n) // factorial(r) // factorial(n - r)


# # 2. 재귀로 조건을 계산하는데, 중복이 너무 많아져서 효율이 떨어진다.
# # 바로 부분문제의 중복(overlapping subproblems)으로 이 때문에 함수의 성능이 치명적으로 나쁘다.
# def bino_coef(n, k):
#     if k == 0 or n == k:  # 조합론에서 n개중 0개 뽑기 or n개중 n개 뽑기
#         return 1

#     # 이항정리 nCk = n-1Ck + n-1Ck-1
#     return bino_coef(n-1, k) + bino_coef(n-1, k-1)


# 2. dp1 - 이항계수의 성질을 이용하자.
def bino_coef(n, k):
    # 1) cache를 만든다. (0~n) (0~k) -> (n+1)*(k+1)
    cache = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

    # 2)
    for i in range(n + 1):
        cache[i][0] = 1
    for i in range(k + 1):
        cache[i][i] = 1

    # 3)
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            cache[i][j] = cache[i - 1][j] + cache[i - 1][j - 1]

    print(cache)
    return cache[n][k]


print(bino_coef(9, 3))

# python에서의 2차원 배열
# cache = [[0 for _ in range(3)] for _ in range(4)]


# 3. pick 하는 방법
def bino_coef(n, k):
    if k > n:
        return 0

    cache = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]

    def choose(times, got):
        if times == n:
            return got == k

        if cache[times][got] != -1:
            return cache[times][got]

        cache[times][got] = choose(times + 1, got) + choose(times + 1, got + 1)
        # print(cache)
        return cache[times][got]

    return choose(0, 0)


print(bino_coef(100, 80))
