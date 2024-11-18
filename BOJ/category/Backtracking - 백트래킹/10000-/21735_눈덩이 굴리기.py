# 2024.11.09 SAT
# https://www.acmicpc.net/problem/21735

"""
눈덩이가 끝에 도달 / 시간이 끝난 경우 종료
눈덩이의 시작 1, 시작위치 0
눈덩이를 굴리는 방법 두 가지
1. +1 위치로 이동 a[i+1] 만큼의 눈덩이 크기 증가
2. +2 위치로 이동 원래 눈덩이의 1/2후 a[i+2] 만큼 눈덩이 크기 증가. 소수점은 절사한다.
"""
import sys

input = sys.stdin.readline


def snowball(pos, size, time):
    if pos == N or time == M:
        return size

    # 1.
    rst = snowball(pos + 1, size + a[pos], time + 1)
    # 2.
    if pos + 2 <= N:
        rst = max(rst, snowball(pos + 2, size // 2 + a[pos + 1], time + 1))

    return rst


N, M = map(int, input().split())
a = list(map(int, input().split()))
print(snowball(0, 1, 0))
