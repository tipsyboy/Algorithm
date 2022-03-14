import sys

input = sys.stdin.readline


def solution():
    n = int(input())
    room = list(map(int, input().split()))
    b, c = map(int, input().split())
    count = 0

    for i in range(n):
        count += 1  # 총 감독관 1명
        r = room[i] - b
        if r > 0:
            count += r // c
            if r % c > 0:
                count += 1

    return count


print(solution())
