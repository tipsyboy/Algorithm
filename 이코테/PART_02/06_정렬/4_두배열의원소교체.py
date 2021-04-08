n, k = map(int, input().split())

arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))

arr_a = sorted(arr_a)
arr_b = sorted(arr_b, reverse=True)

for i in range(k):
    if arr_a[i] < arr_b[i]:
        arr_a[i], arr_b[i] = arr_b[i], arr_a[i]
    else:
        break
        # 최대 k번까지 바꾸겠지만 현재 항에서 오름차순으로 정렬된 A가 이미 크다면 이후는 판별 하지 않아도 됨.

print(arr_a)
print(sum(arr_a))
