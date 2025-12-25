import sys

input = sys.stdin.readline


def binary_search(lo, hi, target) -> int:
    while lo < hi:
        mid = (lo + hi) // 2

        if target > dp[mid]:
            lo = mid + 1
        else:
            hi = mid

    return hi


N = int(input())
arr = []
for _ in range(N):
    a, b = map(int, input().split())
    arr.append((a, b))
arr.sort(key=lambda x: x[0])

dp = [arr[0][1]]
for i in range(1, N):
    if dp[-1] < arr[i][1]:
        dp.append(arr[i][1])
    else:
        idx = binary_search(0, len(dp) - 1, arr[i][1])
        dp[idx] = arr[i][1]

print(N - len(dp))


"""
    2565. 전깃줄    

    1. lis 기초적인 문제, 전봇대 번호 순서대로 정렬 후에 위치를 찾아준다. 

    2. dp를 이용해서 n^2으로 풀어낸다면, 자신보다 앞선 것들 중 값이 작으면서 dp값이 가장 큰 것을 찾아서 더해주면된다. 
"""