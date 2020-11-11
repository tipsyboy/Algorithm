# 통계학
# 산술평균, 중앙값, 최빈값, 범위
# 리스트의 빈도수를 세기위해서 collections 모듈의 Counter class import
import sys
from collections import Counter


def mean(numbers):
    sum_ = 0
    for number in numbers:
        sum_ += number

    return round(sum_ / len(numbers))


def median(numbers):
    numbers.sort()
    # numbers = sorted(numbers)  # .sort() 와 sorted()의 차이
    mid = len(numbers) // 2

    return numbers[mid]


def mode(numbers):
    freq = Counter(numbers).most_common()  # 이미 median()에서 정렬이 되어있음.

    if len(freq) > 1:
        if freq[0][1] == freq[1][1]:  # 두 번째 최빈값을 출력하기 위함
            return freq[1][0]
        else:
            return freq[0][0]
    else:
        return freq[0][0]


def range_num(numbers):
    return max(numbers) - min(numbers)


n = int(sys.stdin.readline())
numbers = [int(sys.stdin.readline()) for i in range(n)]  # number list

print(mean(numbers))
print(median(numbers))
print(mode(numbers))
print(range_num(numbers))
