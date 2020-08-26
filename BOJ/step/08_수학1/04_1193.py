
# 짝수/홀수층 순서가 다르다.
# 이전까지 몇개의 분수를 거쳐왔는가?

import sys

input_num = int(sys.stdin.readline())

layer = 1  # 층 수

while True:
    if input_num > (layer*(layer+1))/2:  # 시그마 k: 1~n
        layer += 1
        continue

    # 현재 층에서 몇 번째 분수인가?
    # input_num 에서 바로 이전 층까지 지나온 수를 빼서 구해줌
    gap = input_num - int(((layer-1)*layer) / 2)

    if layer % 2 == 0:  # 짝수 층
        denominator = layer + 1 - gap   # 분모
        numerator = gap  # 분자
    else:  # 홀수 층
        denominator = gap  # 분모
        numerator = layer + 1 - gap  # 분자

    break

print(f"{numerator}/{denominator}")
