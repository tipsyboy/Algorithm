n = int(input())
houses = list(map(int, input().split()))

houses.sort()
print(houses[(n - 1) // 2])

# 중간 값이 항상 다른 점으로 가는 값의 가장 최소 값이 된다.
# 따라서 리스트를 정렬한 후 n-1//2의 인덱스의 값을 출력한다.
