# ## 1
# # 문제 그대로 조건
# t = int(input())


# for i in range(t):
#     floor = int(input())
#     room_unit = int(input())  # room number
#     prev_floor = [i for i in range(1, room_unit + 1)]

#     for j in range(floor):
#         temp = [0 for i in range(room_unit)]
#         for k in range(room_unit):
#             temp[k] = sum(prev_floor[:k+1])
#         prev_floor = temp

#     print(prev_floor[-1])


# 2
t = int(input())


for i in range(t):
    floor = int(input())
    room_unit = int(input())  # room number
    prev_floor = [i for i in range(1, room_unit + 1)]

    for j in range(floor):
        for k in range(1, room_unit):
            prev_floor[k] += prev_floor[k-1]

    print(prev_floor[-1])
