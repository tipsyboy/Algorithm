# 1) 5kg을 많이 가져가는게 봉지 개수에서 이득
# 2) 이후에 부정방정식 해법처럼

import sys

N = int(sys.stdin.readline())  # 배달 해야하는 설탕의 양(kg)

sugar_box = 0  # 봉지의 총 갯수

while True:
    if N % 5 == 0:  # 5로 나누어 떨어지면,
        sugar_box += N//5  # 몫 만큼 설탕봉지 -> 종료
        break

    if N - 3 < 0:  # 설탕의 무게가 -일 경우, 정확하게 Nkg를 못만드는 경우이다.
        sugar_box = -1
        break

    N = N - 3  # 3kg 봉지 하나 추가
    sugar_box += 1

print(sugar_box)


# import sys

# N = int(sys.stdin.readline())

# sugar_box_3 = 0
# sugar_box_5 = 0

# while True:
#     if N % 5 == 0:
#         sugar_box_5 += N//5
#         break

#     if N-3 < 0:
#         sugar_box_3 = -1
#         sugar_box_5 = -1
#         break

#     N = N - 3
#     sugar_box_3 += 1

# print(
#     f"3kg: {sugar_box_3} / 5kg: {sugar_box_5} / total: {sugar_box_3 + sugar_box_5}")
