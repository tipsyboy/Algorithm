# self number 만들기
# [1, N]의 범위에서 self number를 내보내는 함수
import sys


def is_self_num(max_num):
    num_set = set(range(1, max_num+1))
    self_number = set()

    for num in num_set:
        for j in str(num):
            num += int(j)
        self_number.add(num)

    return sorted(num_set - self_number)


# N = int(sys.stdin.readline()) # 범위 입력 받기
# self_number = is_self_num(N)

self_number = is_self_num(10000)

for i in self_number:
    print(i)
