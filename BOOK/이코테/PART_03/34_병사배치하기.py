import sys
from bisect import bisect_left

input = sys.stdin.readline


def solution1(n, soldiers):
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if soldiers[i] < soldiers[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return n - max(dp)


def solution2(n, soldiers):
    soldiers_revered = list(reversed(soldiers))
    dp = [soldiers_revered[0]]

    for i in range(1, n):
        if soldiers_revered[i] > dp[-1]:
            dp.append(soldiers_revered[i])
            continue

        dp[bisect_left(dp, soldiers_revered[i])] = soldiers_revered[i]

    # print(dp)
    return n - len(dp)


n = int(input())
soldiers = list(map(int, input().split()))

# print(solution1(n, soldiers))
print(solution2(n, soldiers))


"""
34. 병사 배치하기 
    - "가장 긴 감소하는 부분 수열과" 같은 문제

    - i 번째 병사가 무조건 포함된다고 생각하고 i 번째 까지 가장 긴 감소하는 부분수열을 찾는다. 
      1) i 번째 전까지 가장 길면서, i 번째 값보다 큰 전투력의 병사의 dp를 찾고
      2) i의 dp값과의 비교를 통해서 찾아 나간다. 

      1)에서 찾은 값에서 +1은 자기 자신이 부분수열에 무조건 포함되어야 하기 때문

    - 문제에서는 전투력대로 병사를 세우기를 원하고 있기 때문에 n - 가장 긴 수열이 답이된다.
"""
