

# # 정n각 배열 초기화
# nnArray = temp = [[0 for i in range(n)] for i in range(n)]

# Map[0][:3] = Map[2][:3] = [1] * 3
# Map[1][:3] = [1, 0, 1]


# 1) 1번 풀이
def draw_star(n):
    Map = [[" " for i in range(n)] for i in range(n)]  # n*n의 map을 생성

    if n == 3:
        Map[0][:3] = Map[2][:3] = ["*"] * 3
        Map[1][:3] = ["*", " ", "*"]

        return Map

    m = draw_star(n//3)  # 재귀 호출

    # 이제 m을 받아서 채워 넣고 그 맵을 리턴하면됨
    t = n//3
    for i in range(3):  # 3*3 반복
        for j in range(3):
            if i == 1 and j == 1:  # 중간은 빈칸
                continue
            for k in range(t):
                Map[i*t+k][j*t:j*t+t] = m[k][0:t]  # 이전 배열을 좌표에 맞게 저장한다.

    return Map  # 맵 리턴


n = int(input())
x = draw_star(n)

for i in range(n):
    for j in range(n):
        print(x[i][j], end="")
    print()


# 2) 2차원 배열을 1차원으로 생각해서 풀이 - 훨씬 빠름.

# def draw_stars(n):
#     if n == 3:
#         stars = ["***", "* *", "***"]
#         return stars

#     prev_stars = draw_stars(n//3)  # 이전 항의 stars

#     stars_part1 = []
#     for i in range(n//3):
#         stars_part1.append(prev_stars[i] * 3)

#     blank = " " * (n//3)  # 이전 항 만큼의 공백

#     stars_part2 = []

#     for j in range(n//3):
#         stars_part2.append(prev_stars[j] + blank + prev_stars[j])

#     stars = stars_part1 + stars_part2 + stars_part1

#     return stars


# n = int(input())

# Map = draw_stars(n)
# print("\n".join(Map))
