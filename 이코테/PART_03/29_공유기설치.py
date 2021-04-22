# # 1)
# import sys
# input = sys.stdin.readline


# def set_router(houses, c, start, end):
#     global rst

#     if start > end:
#         return

#     mid = (start + end) // 2
#     pre_router = houses[0]
#     count = 1

#     for i in range(1, len(houses)):
#         if houses[i] - pre_router >= mid:
#             count += 1
#             pre_router = houses[i]

#     if count >= c:
#         rst = mid
#         set_router(houses, c, mid+1, end)
#     else:
#         set_router(houses, c, start, mid - 1)


# n, c = map(int, input().split())
# houses = []
# rst = 0
# for _ in range(n):
#     houses.append(int(input()))

# houses.sort()  # for binary search

# # start = 1
# # end = houses[-1] - houses[0]

# set_router(houses, c, 1, houses[-1] - houses[0])
# print(rst)


# 2)
import sys
input = sys.stdin.readline  # 입력 수가 10만이 넘으면 하는게 확실히 차이나게 빠름

# 자료 입력
n, c = map(int, input().split())
houses = []

for i in range(n):
    houses.append(int(input()))

houses.sort()  # 이진탐색을 위한 sorting
rst = 0  # 결과 값

# 초기 인덱스 설정
start = 1
end = houses[-1] - houses[0]

while start <= end:
    mid = (start + end) // 2  # 현재 기준이 되는 거리 (mid 거리 이상 차이가 나야 설치를 한다는 뜻)
    pre_router = houses[0]  # 이전 공유기가 설치된 집 - 첫 집에는 무조건 설치를 하기 때문에 초기 값 설정
    count = 1  # 공유기의 개수

    # 두 번째 공유기부터 설치를 시작한다
    for i in range(1, n):
        if houses[i] - pre_router >= mid:
            count += 1
            pre_router = houses[i]

    if count >= c:  # 모든 공유기를 다 설치
        rst = mid
        start = mid + 1
    else:  # 할당된 공유기를 설치하지 못한 경우
        end = mid - 1

print(rst)
