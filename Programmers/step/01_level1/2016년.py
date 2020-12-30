def solution(a, b):
    day_names = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # # 1
    # for i in range(a-1):
    #     b += month[i]

    # 2
    b += sum(month[: a - 1])

    return day_names[b % 7 - 1]


# ### 2. 모듈이용
# import datetime


# def solution_2(a, b):
#     day_names = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
#     x = datetime.datetime(2016, a, b).weekday()

#     return day_names[x]

print(solution(5, 24))
