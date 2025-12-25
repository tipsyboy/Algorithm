import sys

input = sys.stdin.readline

N = int(input())
arr = sorted(map(int, input().split()))

ans = 0
for i in range(N):
    target = arr[i]
    left, right = 0, N - 1

    while left < right:
        sumv = arr[left] + arr[right]

        if target == sumv and i != left and i != right:
            ans += 1
            break

        if sumv < target or i == left:
            left += 1
        elif sumv > target or i == right:
            right -= 1
print(ans)

"""
1253. 좋다
    - 투 포인터 / 이분탐색으로 구현할 수 있고, 이분 탐색 구현에서 꽤나 어려움을 겪었음..

    - 이분 탐색시 배열 슬라이싱을 통해서 arr를 재정의 한후에 계속 찾았는데
      슬라이싱, 배열 합치기가 전부 O(n)이란 것을 알게됨 (TLE) 따라서 left, right를 구해서 
      타깃이 되는 값은 제외해 주는 방법을 사용했음

    - 위 코드는 투 포인터 구현이고 
      이 문제에서는 이 방법이 좀 더 직관적, 시간복잡도 이득 으로 투 포인터 구현이 더 알맞다 생각됨
"""
