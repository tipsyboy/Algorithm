# https://www.acmicpc.net/problem/4889

import sys

input = sys.stdin.readline

cmd_cnt = 1
while True:
    command = input().rstrip()

    if command.startswith("-"):
        break

    cnt, ans = 0, 0
    for b in command:
        if b == "{":
            cnt += 1
        else:
            if cnt < 1:
                ans += 1
                cnt += 1
            else:
                cnt -= 1

    ans += cnt // 2

    print(f"{cmd_cnt}. {ans}")
    cmd_cnt += 1
