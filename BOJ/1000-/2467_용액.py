import sys

input = sys.stdin.readline


def two_pointer(N, arr) -> list:
    left, right = 0, N - 1
    minv = float("inf")
    ans = [0, 0]

    while left < right:
        temp = arr[left] + arr[right]
        if minv > abs(temp):
            minv = abs(temp)
            ans[0], ans[1] = left, right

        if temp < 0:
            left += 1
        elif temp > 0:
            right -= 1
        else:
            return [arr[ans[0]], arr[ans[1]]]

    return [arr[ans[0]], arr[ans[1]]]


N = int(input())
arr = sorted(map(int, input().split()))
print(*two_pointer(N, arr))


# # 2. 이분 탐색 풀이
# import sys

# input = sys.stdin.readline


# def binary_search(now, left, right) -> int:
#     minv = float("inf")
#     min_idx = right

#     while left <= right:
#         mid = (left + right) // 2
#         if minv > abs(now + arr[mid]):
#             minv = abs(now + arr[mid])
#             min_idx = mid

#         if now + arr[mid] < 0:
#             left = mid + 1
#         elif now + arr[mid] > 0:
#             right = mid - 1
#         else:
#             return min_idx

#     return min_idx


# N = int(input())
# arr = sorted(map(int, input().split()))
# rst = float("inf")
# ans = [0, 0]
# for i in range(N - 1):
#     min_idx = binary_search(arr[i], i + 1, N - 1)
#     if rst > abs(arr[i] + arr[min_idx]):
#         rst = abs(arr[i] + arr[min_idx])
#         ans[0], ans[1] = i, min_idx

# print(arr[ans[0]], arr[ans[1]])

"""
2467. 용액
    - 투 포인터, 이분 탐색 두 방식으로 풀이할 수 있지만, 투 포인터에 더 가까운 문제라고 생각함

    1. 투 포인터
    - 정렬된 배열의 양 끝값으로 포인터를 초기화하고 값의 합이 0보다 [큰/작]에 따라서 각각의 포인터를 옮겨 나간다.
      각 시도에서 abs값을 비교해서 최적해를 찾아 나가면 된다. 
      O(n)?
    
    2. 이분 탐색
    - 정렬된 배열의 값을 순차적으로 i번째 값과의 합을 통해서 최적해를 찾는다. 
      i번 값과의 최적 값을 찾을때 이분 탐색이 사용된다. 
      O(nlogn)
"""