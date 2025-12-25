# https://www.acmicpc.net/problem/19583

import sys

input = sys.stdin.readline


def convert_time(t: str) -> int:
    h, m = t.split(":")

    return int(h) * 100 + int(m)


S, E, Q = map(convert_time, input().split())
meeting = set()
ans = 0
while True:
    chat_log = input().rstrip()
    if chat_log == "":
        break

    time, nick = chat_log.split()
    time = convert_time(time)

    if time <= S:
        meeting.add(nick)
    elif E <= time <= Q and nick in meeting:
        ans += 1
        meeting.remove(nick)

print(ans)