import sys

input = sys.stdin.readline


def binary_search(S, lo, hi) -> int:
    ans = -1

    while lo <= hi:
        mid = (lo + hi) // 2

        if mid * (mid + 1) // 2 <= S:
            ans = max(ans, mid)
            lo = mid + 1
        else:
            hi = mid - 1

    return ans


S = int(input())
print(binary_search(S, 1, S))


"""
1789. 수들의 합
    - 서로 다른 N개의 자연수의 합이 S가 되는 N의 최댓값을 찾는 문제, 처음에 문제 이해가 어려웠음..

    - 서로 다른 N개의 자연수의 수열을 A라고 할때, A의 합이 될 수 있는 가장 작은 값은 N * (N + 1) // 2가 된다. 
      수열A의 가장 큰 수가 N일때가 수열A의 합의 최솟값이기 때문 (1,2,3 .... N)
      
      따라서 이분탐색을 통해서 S보다 작은 N을 찾아 나간다. 
"""