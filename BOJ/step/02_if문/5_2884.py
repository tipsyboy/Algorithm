# 1번 풀이

hour, minute = map(int, input().split())

if minute < 45:
    minute += 15  # 60 + (minute - 45)
    hour -= 1
    if hour < 0:
        hour += 24
else:
    minute -= 45

print(hour, minute)


# 2번 풀이

# hour,minute = map(int, input().split())

# if minute > 44:
#     print(hour, minute - 45)
# elif minute <= 44 and hour >= 1:
#     print(hour - 1, minute + 15)
# else:
#     print(23, minute + 15)
