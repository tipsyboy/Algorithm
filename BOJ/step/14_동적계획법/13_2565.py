import sys

n = int(sys.stdin.readline())  # 줄 수
wire_lst = []  # 줄 리스트

# 입력
for i in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    wire_lst.append(temp)

# A 전봇대를 기준으로 정렬한다.
wire_lst_sorted = sorted(wire_lst, key=lambda wire: wire[0])  # 람다식 사용방법 익혀둘 것

dp = [0 for i in range(n)]

for i in range(n):
    dp_max = 0
    for j in range(i):
        if wire_lst_sorted[i][1] > wire_lst_sorted[j][1]:
            dp_max = max(dp_max, dp[j])

    dp[i] = dp_max + 1

print(n - max(dp))
