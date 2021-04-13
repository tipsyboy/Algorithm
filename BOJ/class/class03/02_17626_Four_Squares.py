# 1)
import time

start = time.time()
n = int(input())
min_value = 4  # 라그랑주 제곱수 최대개수는 4로 밝혀져있다.
# n = a^2 + b^2 + c^2 + d^2

for a in range(int(n ** 0.5), int((n // 4) ** 0.5), -1):
    if n == a * a:
        min_value = 1
        break
    else:
        temp = n - a * a

        for b in range(int(temp ** 0.5), int((temp // 3) ** 0.5), -1):
            if n == a * a + b * b:
                min_value = min(min_value, 2)
            else:
                temp = n - a * a - b * b

                for c in range(int(temp ** 0.5), int((temp // 2) ** 0.5), -1):
                    if n == a * a + b * b + c * c:
                        min_value = min(min_value, 3)

print(min_value)
print(time.time() - start)

# # 2) dp - 시간초과..
# import time
# n = int(input())
# start = time.time()
# dp = [0, 1]

# for i in range(2, n + 1):
#     min_value = 1e9
#     # a = int(i**0.5)
#     # if not a:
#     #     a = 1

#     # while a*a <= i:
#     #     min_value = min(min_value, dp[i - a*a])
#     #     a += 1

#     for a in range(int(i**0.5), int((i//2)**0.5), -1):
#         min_value = min(min_value, dp[i-a*a])
#         if min_value == 0:
#             break

#     dp.append(min_value + 1)

# # print(dp)
# print(dp[n])
# print(time.time() - start)
