# 1) 조합의 정의
def factorial(n):
    rst = 1

    for i in range(1, n+1):
        rst *= i

    return rst


def bino_coef_factorial(n, k):

    return factorial(n) // factorial(k) // factorial(n-k)


# 2) 재귀 - 이항계수의 성질 이용하기
def bino_coef_recursion(n, k):
    # nC0, nCn = 1
    if k == 0 or k == n:
        return 1

    return bino_coef_recursion(n-1, k) + bino_coef_recursion(n-1, k-1)


# 3) 메모이제이션 - 이항계수의 성질 이용하기
def bino_coef(n, k):
    cache = [[0 for _ in range(k+1)] for _ in range(n+1)]

    # nC0, nCn 설정
    for i in range(n+1):
        cache[i][0] = 1
    for i in range(k+1):
        cache[i][i] = 1

    for i in range(1, n+1):
        for j in range(1, k+1):
            cache[i][j] = cache[i-1][j] + cache[i-1][j-1]

    return cache[n][k]


# 4) 메모이제이션2
def bino_coef_2(n, k):
    # 조합 정의에 맞지 않는 입력 값 제거
    if k > n:
        return 0

    cache = [[-1 for _ in range(n+1)] for _ in range(n+1)]

    def choose(times, got):
        # 뽑는 기회를 다 사용했을 때, 원래 뽑고자 하는 수 많큼 뽑았으면 return True
        if times == n:
            return got == k

        # 이미 계산된 결과가 있는 경우
        if cache[times][got] != -1:
            return cache[times][got]

        cache[times][got] = choose(times+1, got) + choose(times+1, got+1)

        return cache[times][got]

    return choose(0, 0)


n, k = map(int, input().split())
# print(bino_coef_factorial(n, k)) # 1) 수가 너무 커서 오버플로우 발생 위험
# print(bino_coef_recursion(n, k))  # 2) 부문 문제의 중복 문제 때문에 중복 연산량이 많아서 느리다.
# print(bino_coef(n, k))  # 3)
print(bino_coef_2(n, k))
