"""
- 정렬 기준을 함수로 작성해서 커스텀 정렬을 수행 할 수 있다.

- 참조 문제: https://www.acmicpc.net/problem/1431
"""

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
