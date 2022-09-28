import sys

input = sys.stdin.readline


def condition2(number: str) -> int:
    sumv = 0
    for num in number:
        if num.isnumeric():
            sumv += int(num)

    return sumv


N = int(input())
serial_numbers = []
for _ in range(N):
    serial_numbers.append(input().rstrip())

serial_numbers.sort(key=lambda x: (len(x), condition2(x), x))
print("\n".join(serial_numbers))


"""
1431. 시리얼 번호
    - 파이썬 내장함수 sort(), sorted()는 조건 람다식에 함수를 집어넣어 커스텀 할 수 있다. 
"""