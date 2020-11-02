# import sys


# # def digit_len(n):
# #     digit = 0

# #     while n:
# #         n //= 10
# #         digit += 1

# #     return digit


# N = int(sys.stdin.readline())
# # digit = digit_len(N) # 처음에 자릿수 구했던 방식
# result = 0

# for i in range(1, N):
#     digit = len(str(i))
#     digit_n = 10 ** (digit-1)

#     temp = i
#     _sum = 0
#     _sum += temp
#     for j in range(digit-1):
#         _sum += (temp // digit_n)
#         temp %= digit_n
#         digit_n = int(digit_n / 10)

#     _sum += temp  # 나머지를 더해
#     if _sum == N:
#         result = i
#         break

# print(result)


# # 2) 함수
# import sys


# def devide_sum(num):
#     devided_num = list(map(int, str(num)))

#     return num + sum(devided_num)


# N = int(sys.stdin.readline())
# result = 0

# while True:
#     d_sum = devide_sum(result)
#     if d_sum == N:
#         break

#     result += 1
#     if result == N:  # 생성자가 없는 경우
#         result = 0
#         break

# print(result)


# 3) 최소 생성자 값을 생각하는 경우 - 매우빠름
import sys


def get_constructor(start, N):
    for num in range(start, N):
        devide_sum = num  # 자기 자신 더함
        temp = list(map(int, str(num)))  # 각 자릿수 리스트 만들고
        devide_sum += sum(temp)  # 각 자릿수 더함

        # num의 분해 합이 주어진 분해합 N과 같으면 생성자.
        if devide_sum == N:
            return num

    return 0  # 전부 돌았는데 결과가 없으면 생성자가 없음


N = int(sys.stdin.readline())
start = N - len(str(N)) * 9  # 생성자가 될 수 있는 최소값

if start < 1:  # 0, 음수인 경우
    start = 1

constructor_min = get_constructor(start, N)
print(constructor_min)
