n = int(input())
arr = [0] * 1000001  # 문제의 범위에 맞게 초기화

# 가게에 있는 전체 부품
for i in input().split():
    arr[int(i)] = 1

m = int(input())
x = list(map(int, input().split()))

for part in x:
    if arr[part] == 1:
        print("yes", end=" ")
    else:
        print("no", end=" ")
