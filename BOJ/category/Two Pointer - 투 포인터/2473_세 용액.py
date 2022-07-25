import sys

input = sys.stdin.readline
INF = float("inf")


def two_pointer(fixed, left, right) -> list:
    rst = INF
    l, r = left, right

    while left < right:
        temp = arr[fixed] + arr[left] + arr[right]
        if abs(temp) < rst:
            rst = abs(temp)
            l, r = left, right

        if temp < 0:
            left += 1
        elif temp > 0:
            right -= 1
        else:
            return [rst, l, r]

    return [rst, l, r]


N = int(input())
arr = list(map(int, input().split()))
arr.sort()

ans_val = INF
ans = [-1, -1, -1]
for fixed in range(N - 2):
    rst_val = two_pointer(fixed, fixed + 1, N - 1)

    if rst_val[0] < ans_val:
        ans_val = rst_val[0]
        ans[0], ans[1], ans[2] = arr[fixed], arr[rst_val[1]], arr[rst_val[2]]

    if rst_val[0] == 0:
        break


ans.sort()
print(*ans)


"""
2473. 세 용액
    - 두 용액 시리즈와 거의 유사한 문제 
      한 용액을 고정해두고, 나머지 두 용액을 투포인터로 최적해를 찾아나가는 방식을 사용한다.
"""