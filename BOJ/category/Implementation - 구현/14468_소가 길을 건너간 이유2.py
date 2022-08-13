# https://www.acmicpc.net/problem/14468
# 2022-08-13 Sat

import sys

input = sys.stdin.readline

input_string = input().rstrip()
start = dict()
end = dict()
road = set()
for i in range(52):
    if input_string[i] not in road:
        start[input_string[i]] = i
        road.add(input_string[i])
    else:
        end[input_string[i]] = i

cnt = 0
for i in range(26):
    for j in range(26):
        if i == j:
            continue

        if (
            start[chr(i + 65)] < start[chr(j + 65)]
            and start[chr(j + 65)] < end[chr(i + 65)]
            and end[chr(i + 65)] < end[chr(j + 65)]
        ):
            cnt += 1

print(cnt)

"""
14468. 소가 길을 건너간 이유2
    - 교집합의 범위에 대해서 잘 생각해보자
"""