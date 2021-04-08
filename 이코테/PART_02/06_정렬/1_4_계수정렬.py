arr = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

# 모든 원소의 범위를 포함하는 배열을 선언 후 , 0으로 초기화
count = [0] * (max(arr) + 1)

# 원시 배열의 원소의 개수를 각각 셈
for i in range(len(arr)):
    count[arr[i]] += 1

# 출력
for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=" ")
