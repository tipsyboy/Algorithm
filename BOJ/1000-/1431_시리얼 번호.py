# https://www.acmicpc.net/problem/1431

import sys

input = sys.stdin.readline


def compare_numbers(serial: str) -> int:
    sumv = 0
    for elem in serial:
        if not elem.isnumeric():
            continue
        sumv += int(elem)

    return sumv


N = int(input())
serials = []
for _ in range(N):
    serials.append(input().rstrip())

serials.sort(key=lambda x: (len(x), compare_numbers(x), x))
print("\n".join(serials))


"""
1431. 시리얼 번호
    - 파이썬 내장함수 sort(), sorted()는 조건 람다식에 함수를 집어넣어 커스텀 할 수 있다. 
"""