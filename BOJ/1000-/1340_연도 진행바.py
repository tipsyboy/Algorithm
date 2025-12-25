# 2024.06.07 FRI
# https://acmicpc.net/problem/1340

import sys

input = sys.stdin.readline
MONTH_DAYS = {
    "January": 31,
    "February": 28,
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31,
}

month, day, year, hm = input().split()
day = int(day.rstrip(","))
year = int(year)
hour, minute = map(int, hm.split(":"))

total = 365 * 24 * 60
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:  # 윤년 하루 추가
    MONTH_DAYS["February"] += 1
    total += 24 * 60

gone = 0
for m, v in MONTH_DAYS.items():  # dict 순서 보장성
    if month == m:
        break
    gone += v * 24 * 60

gone += (day - 1) * 24 * 60
gone += hour * 60
gone += minute
print(gone / total * 100)
