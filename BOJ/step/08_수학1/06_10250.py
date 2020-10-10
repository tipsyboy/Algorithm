import sys


T = int(sys.stdin.readline())  # 테스트 케이스


for i in range(T):
    # 호수, 높이, n번째 손님
    H, W, N = map(int, sys.stdin.readline().split())

    # 문제에서 조건 제거
    # if W*H < N:
    #   print("수용 못함.")

    # 나누어 떨어지는 경우
    if N % H == 0:
        x = N // H  # x: 호수
        y = H  # 층수
    else:
        x = N // H + 1  # x: 호수
        y = N % H

    print(y * 100 + x)
