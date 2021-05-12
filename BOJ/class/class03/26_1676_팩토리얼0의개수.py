# 1) 그냥 풀기
def count_zero(n):
    five = 0

    for i in range(1, n + 1):
        while i % 5 == 0:
            five += 1
            i //= 5

    return five


# 2) memoiztion을 이용해서 해결하기
def count_trailing_zero(n):
    cache = [-1] * (n + 1)
    rst = 0  # 결과 값 - 팩토리얼의 0의 개수

    def count_factors(x, f):
        if cache[x] != -1:
            return cache[x]

        cache[x] = count_factors(x // f, f) + 1 if x % f == 0 else 0

        return cache[x]

    for i in range(1, n + 1):
        rst += count_factors(i, 5)

    return rst


# 3) factorial 범위에서 5의 제곱수를 배수로 갖는 수 찾기
def count_zero_sq(n):
    flag = 5
    count = 0

    while flag <= n:
        count += n//flag
        flag *= 5

    return count


n = int(input())
print(count_zero_sq(n))
