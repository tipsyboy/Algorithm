# 1. is_Prime 함수를 이용 - 제곱수까지만 검증

# def is_Prime(num):
#     if num <= 1:
#         return False

#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:  # 나누어 떨어지는게 있는 경우
#             return False

#     return True


# M, N = map(int, input().split())  # 정수
# prime_number = []

# for i in range(M, N+1):
#     if is_Prime(i):
#         prime_number.append(i)

# for prime in prime_number:
#     print(prime)


# 2. 에라토스테네스의 체 (Sieve of Eratosthenes) + 제곱수 이용
def Eratos(M, N):
    prime_number = [False, False] + [True] * (N-1)  # list 생성 (체 생성)

    for i in range(2, int(N**0.5) + 1):  # 제곱근까지 검증
        if prime_number[i]:  # 체에 걸러지지 않은 수인 경우에,
            for j in range(2*i, N+1, i):  # 자신을 제외한 배수를 모두
                prime_number[j] = False  # 제거한다.

    return prime_number  # 리스트를 리턴


# 출력
M, N = map(int, input().split())
x = Eratos(M, N)
for i in range(M, N+1):
    if x[i]:
        print(i)
