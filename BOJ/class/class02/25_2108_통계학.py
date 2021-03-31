import sys
from collections import Counter
input = sys.stdin.readline


# 산술 평균
def mean(numbers):
    return round(sum(numbers) / len(numbers))


# 중앙 값 - n이 홀수라고 가정한다.
def median(numbers):
    temp = sorted(numbers)

    return temp[len(temp) // 2]


def mode(numbers):
    temp = sorted(numbers)
    mode_dict = Counter(temp).most_common()

    if len(numbers) > 1:
        if mode_dict[0][1] == mode_dict[1][1]:
            mod = mode_dict[1][0]
        else:
            mod = mode_dict[0][0]
    else:
        mod = mode_dict[0][0]

    return mod


def scope(numbers):
    return max(numbers) - min(numbers)


n = int(input())
numbers = []

for _ in range(n):
    numbers.append(int(input()))

print(mean(numbers))
print(median(numbers))
print(mode(numbers))
print(scope(numbers))
