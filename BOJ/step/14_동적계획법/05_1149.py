import sys

n = int(sys.stdin.readline())  # 집의 개수

# 집의 비용 입력
cost_RGB_home = []
for i in range(n):
    cost_RGB_home.append(list(map(int, sys.stdin.readline().split())))

cost_RGB_min = cost_RGB_home[0]

for i in range(1, n):
    temp_lst = []

    # 이번에 R이 올 차례
    temp = min(cost_RGB_min[1], cost_RGB_min[2])
    temp = temp + cost_RGB_home[i][0]
    temp_lst.append(temp)

    # 이번에 G가 올 차례
    temp = min(cost_RGB_min[0], cost_RGB_min[2])
    temp = temp + cost_RGB_home[i][1]
    temp_lst.append(temp)

    # 이번에 B가 올 차례
    temp = min(cost_RGB_min[0], cost_RGB_min[1])
    temp = temp + cost_RGB_home[i][2]
    temp_lst.append(temp)

    cost_RGB_min = temp_lst

print(min(cost_RGB_min))
