# # 1
# n = int(input())
# INF = int(1e9)
# rst = INF  # INF 초기 값
# sugar5 = 0
# while True:
#     temp = n

#     temp -= sugar5 * 5
#     if temp < 0:
#         break

#     if temp % 3 == 0:
#         sugar3 = temp // 3
#         if rst > sugar3 + sugar5:
#             rst = sugar3 + sugar5
#         sugar5 += 1
#     else:
#         sugar5 += 1


# if rst == INF:
#     print(-1)
# else:
#     print(rst)


# 2
sugar = int(input())

bag = 0

while sugar >= 0:
    if sugar % 5 == 0:
        bag += sugar // 5
        print(bag)
        break

    sugar -= 3
    bag += 1

    if sugar < 0:
        print(-1)
        break
