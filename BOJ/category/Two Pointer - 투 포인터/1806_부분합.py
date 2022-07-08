import sys

input = sys.stdin.readline
INF = float("inf")


def solution1(N, arr) -> int:
    left, right = 0, 0
    sumv = arr[0]
    ans = INF

    while left <= right:
        if sumv >= S:
            ans = min(ans, right - left + 1)
            sumv -= arr[left]
            left += 1
        else:
            right += 1
            if right > N - 1:
                break
            sumv += arr[right]

    if ans == INF:
        ans = 0
    return ans


def solution2(N, arr) -> int:
    psum = [0]
    for i in range(N):
        psum.append(psum[-1] + arr[i])

    left, right = 0, 1
    ans = INF
    while right < N + 1 and left < right:
        sumv = psum[right] - psum[left]

        if sumv >= S:
            ans = min(ans, right - left)
            left += 1
        else:
            right += 1

    if ans == INF:
        ans = 0
    return ans


N, S = map(int, input().split())
arr = list(map(int, input().split()))
# print(solution1(N, arr))
print(solution2(N, arr))

"""
1806. 부분합
    - 투 포인터로 해결
      구간의 값을 갱신하면서 포인터들을 옮겨다니면됨

    - solution2()의 경우는 prefix sum을 미리 구해두고 해결하는 방식
"""