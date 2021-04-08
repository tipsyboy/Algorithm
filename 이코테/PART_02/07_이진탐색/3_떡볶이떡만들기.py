n, m = map(int, input().split())
dduck_list = list(map(int, input().split()))

start = 0
end = max(dduck_list)

while start <= end:
    total = 0  # 떡 길이
    mid = (start + end) // 2

    for dduck in dduck_list:
        if dduck > mid:
            total += dduck - mid

    if total < m:
        end = mid - 1
    else:
        result = mid  # mid의 값은 시간이 지날수록 '최적화된 값'을 찾는다.
        start = mid + 1

print(result)
