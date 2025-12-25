# 2024.08.28 WED
# https://www.acmicpc.net/problem/1089

import sys

input = sys.stdin.readline
NUMBERS = {
    0: "####.##.##.####",
    1: "..#..#..#..#..#",
    2: "###..#####..###",
    3: "###..####..####",
    4: "#.##.####..#..#",
    5: "####..###..####",
    6: "####..####.####",
    7: "###..#..#..#..#",
    8: "####.#####.####",
    9: "####.####..####",
}


def get_valid_numbers(target):
    # 각 번호 안내판 숫자의 가능한 수를 찾아냄
    rst = []
    for i in range(10):
        valid = True
        for j in range(15):
            if NUMBERS[i][j] == "." and target[j] == "#":
                valid = False
                break

        if valid:
            rst.append(i)

    return rst


N = int(input())
light = [list(input().rstrip()) for _ in range(5)]

# 각 번호 안내판 숫자의 가능한 수를 찾아냄
candidates = []
for i in range(N):
    num = ""
    for row in range(5):
        for col in range(4 * i, 4 * i + 3):
            num += light[row][col]

    candidates.append(get_valid_numbers(num))

# 나타날 수 있는 숫자의 총 개수
total = 1
for i in range(len(candidates)):
    total *= len(candidates[i])

if total:
    ans = 0
    for i in range(len(candidates)):
        cnt = total // len(candidates[i])  # 수의 등장 횟수

        for num in candidates[i]:
            ans += cnt * num * (10 ** (N - i - 1))
    print(ans / total)
else:
    print(-1)
