# 2024.08.03 SAT
# https://www.acmicpc.net/problem/9367

import sys
from math import ceil

input = sys.stdin.readline


def rented(car_name):
    return cars[car_name][3] == "F"


def is_renter(name):
    return name in renter


T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    cars = dict()

    for __ in range(n):
        N, p, q, k = input().split()
        cars[N] = [int(p), int(q), int(k), "T"]

    renter = dict()
    result = dict()
    for __ in range(m):
        t, S, e, com = input().split()  # 시간, 이름, 사건, 커맨드
        if S in result and result[S] == -1:
            continue

        if e == "p":
            if com not in cars or is_renter(S):  # 없는 차 or 이미 빌린 사람 or 이미 빌려간 차
                # or rented(com):
                result[S] = -1
                continue
            renter[S] = com
            cars[com][3] = "F"
        elif e == "r":
            if S not in renter:  # 차를 빌린적이 없음.
                result[S] = -1
                continue

            car_name = renter[S]
            result[S] = result.get(S, 0) + cars[car_name][1] + int(com) * cars[car_name][2]
            cars[car_name][3] = "T"
            del renter[S]
        elif e == "a":
            if S not in renter:
                result[S] = -1
                continue
            car_name = renter[S]
            result[S] = result.get(S, 0) + ceil(cars[car_name][0] * int(com) / 100)

    for renter_name in renter.keys():
        result[renter_name] = -1

    result = sorted(result.items())
    for name, rst in result:
        if rst == -1:
            print(name, "INCONSISTENT")
        else:
            print(name, rst)
