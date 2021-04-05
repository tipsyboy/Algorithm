import sys

# from collections import Counter
input = sys.stdin.readline

n, m, block = map(int, input().split())
house_site = []
component = dict()
rst = []
min_time = 100000000000000

for _ in range(n):
    row = list(map(int, input().split()))
    for r in row:
        if r in component:
            component[r] += 1
        else:
            component[r] = 1

    house_site.append(row)


for i in range(257):  # i높이로 만들기 위해
    time = 0
    block_temp = block
    for j in component.keys():  # 모든 높이를 i로 만든다.
        # i, j 가 같은 경우
        if i == j:
            continue
        # 높이가 더 높아서 파야 되는 경우 -> 파기 2s
        elif i < j:
            # 2s * (한 개 블록에서 파내는 수)  * (파내야 하는 블록 수)
            time += 2 * (j - i) * component[j]
            block_temp += (j - i) * component[j]
        # 높이가 낮아서 블록을 놓아야 하는 경우 -> 놓기 1s
        else:
            time += 1 * (i - j) * component[j]  # 1s * (한 블록에서 놓아야 하는 수)
            block_temp -= (i - j) * component[j]

    if block_temp >= 0 and time <= min_time:
        min_time = time
        rst.append((time, i))

rst = sorted(rst, key=lambda x: (x[0], -x[1]))  # 시간 오름차순 같은 경우에는 내림차순의 높이
print(rst[0][0], rst[0][1])
