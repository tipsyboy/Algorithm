# # 1) 내 풀이 (통과함)
# from itertools import combinations

# n, m = map(int, input().split())
# city = []
# houses = []
# chicken = []
# # rst = []

# # 맵 설정
# for _ in range(n):
#     temp = list(map(int, input().split()))
#     city.append(temp)

# for i in range(n):
#     for j in range(n):
#         # 집 좌표
#         if city[i][j] == 1:
#             houses.append((i, j))
#         # 치킨집
#         elif city[i][j] == 2:
#             chicken.append((i, j))

# chicken_com = list(combinations(chicken, m))


# rst = 1e9
# for ch_com in chicken_com:
#     sum_length = 0
#     for house in houses:
#         h_x, h_y = house
#         length = 1e9
#         for ch in ch_com:
#             ch_x, ch_y = ch
#             length = min(length, abs(ch_x - h_x) + abs(ch_y - h_y))

#         sum_length += length
#     # rst.append(sum_length)
#     rst = min(rst, sum_length)

# print(rst)
# print(min(rst))


# 2) 책 풀이
from itertools import combinations


n, m = map(int, input().split())
chicken, house = [], []

# 책에서는 맵을 받지 않고 좌표 정보만 추출했음
# 생각 해보니 이게 효율적인게 이 문제에서는 map data를 따로 갖고 있을 필요가 없을 뿐더러 맵을 받은 이후에
# 다시 루프를 돌면서 조회하면 시간이 더 걸림
for r in range(n):
    data = list(map(int, input().split()))
    for c in range(n):
        if data[c] == 1:  # 집인 경우
            house.append((r, c))
        elif data[c] == 2:  # 치킨가게인 경우
            chicken.append((r, c))

# 모든 치킨 집에서 m개를 뽑아서 남길 치킨집의 후보군을 만든다.
# itertools 모듈의 combinations 클래스를 사용함
candidates = list(combinations(chicken, m))


# print(candidates)
# 치킨 거리를 계산하는 함수
def get_sum(candidate):
    result = 0
    for hx, hy in house:
        temp = 1e9
        for cx, cy in candidate:
            temp = min(temp, abs(hx - cx) + abs(hy - cy))

        # 가장 가까운 치킨거리 더하고
        result += temp

    return result


result = 1e9
for candidate in candidates:
    result = min(result, get_sum(candidate))

print(result)


# test case
# 5 3
# 0 0 1 0 0
# 0 0 2 0 1
# 0 1 2 0 0
# 0 0 1 0 0
# 0 0 0 0 2


# 5 2
# 0 2 0 1 0
# 1 0 1 0 0
# 0 0 0 0 0
# 2 0 0 1 1
# 2 2 0 1 2

# 5 1
# 1 2 0 0 0
# 1 2 0 0 0
# 1 2 0 0 0
# 1 2 0 0 0
# 1 2 0 0 0
