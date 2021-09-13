import sys

input = sys.stdin.readline


def two_pointers(n, k, arr):
    max_sum = sum(arr[:k])
    cur_sum = max_sum

    for left in range(n - k):
        right = left + k
        cur_sum = cur_sum + arr[right] - arr[left]
        max_sum = max(max_sum, cur_sum)

    return max_sum


def prefix_sum(n, k, arr):
    psum = [0] * (n + 1)

    for i in range(1, n + 1):
        psum[i] = psum[i - 1] + arr[i - 1]
    max_sum = psum[k]

    for left in range(1, n - k + 1):
        right = left + k
        max_sum = max(max_sum, psum[right] - psum[left])

    return max_sum


n, k = map(int, input().split())
arr = list(map(int, input().split()))

print(two_pointers(n, k, arr))
print(prefix_sum(n, k, arr))


"""
2559. 수열 (Silver 3)
    - index 범위를 계속 잘못 지정해서 골머리좀 앓았음.

    - 구간합을 이용해서 해결하는 방법과 
      합의 중간 값은 변경되지 않고 새로 추가된 값(right)과 빼야되는 값(left) 투 포인터를 이용해서 해결했다. 
"""
