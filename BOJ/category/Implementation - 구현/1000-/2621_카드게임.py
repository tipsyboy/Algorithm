# https://www.acmicpc.net/problem/2621

import sys

input = sys.stdin.readline


def are_straight(nums: list) -> bool:
    s_nums = sorted(map(int, nums))
    if len(s_nums) != 5:
        return False

    for i in range(len(nums) - 1):
        if s_nums[i] + 1 != s_nums[i + 1]:
            return False

    return True


def calc(colors: dict, nums: dict) -> int:
    nums_arr = sorted(nums.items(), key=lambda x: (-x[1], -int(x[0])))

    if max(colors.values()) == 5 and are_straight(nums.keys()):
        return int(nums_arr[0][0]) + 900

    if nums_arr[0][1] == 4:
        return int(nums_arr[0][0]) + 800

    if nums_arr[0][1] == 3 and len(nums_arr) == 2:
        return int(nums_arr[0][0]) * 10 + int(nums_arr[1][0]) + 700

    if len(colors) == 1:
        return int(nums_arr[0][0]) + 600

    if are_straight(nums.keys()):
        return int(nums_arr[0][0]) + 500

    if nums_arr[0][1] == 3:
        return int(nums_arr[0][0]) + 400

    if nums_arr[0][1] == 2 and nums_arr[1][1] == 2:
        return int(nums_arr[0][0]) * 10 + int(nums_arr[1][0]) + 300

    if nums_arr[0][1] == 2:
        return int(nums_arr[0][0]) + 200

    return max(map(int, nums.keys())) + 100


colors = dict()
nums = dict()
for _ in range(5):
    c, n = input().split()
    colors[c] = colors.get(c, 0) + 1
    nums[n] = nums.get(n, 0) + 1

print(calc(colors, nums))
