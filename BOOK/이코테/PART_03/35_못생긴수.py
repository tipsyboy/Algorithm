import sys

input = sys.stdin.readline

n = int(input())

i2, i3, i5 = 0, 0, 0
next2, next3, next5 = 2, 3, 5
dp = [0] * n
dp[0] = 1

for i in range(1, n):
    dp[i] = min(next2, next3, next5)

    if dp[i] == next2:
        i2 += 1
        next2 = dp[i2] * 2
    if dp[i] == next3:
        i3 += 1
        next3 = dp[i3] * 3
    if dp[i] == next5:
        i5 += 1
        next5 = dp[i5] * 5

# print(dp)
print(dp[n - 1])


"""
35. 못생긴 수 (p381)
    1) 최초의 못생긴 수 1을 dp에 추가하고 다음 못생긴 수 후보군을 찾기 위해서 {2, 3, 5}를 곱한다.
       2, 3, 5가 다음 못생긴 수 후보군이 된다. 하지만, 정렬 상태를 유지하면서 dp에 추가하기 위해서
       아직 추가 하지 않는다. 
    2) 정렬상태를 유지하기 위해서 각각에 곱할 수를 가리키기 위한, index pointer i2, i3, i5를 선언하고
       0 index를 가리키게 설정 초기화한다. 
    3) 이제 후보군 {2, 3, 5}에서 최솟값을 선택해서 dp에 추가한다. 
    4) 후보군을 갱신하기 위해서 next가 어떤 수에서 출발했는지 찾아야 한다. 
       dp에 추가된 수를 next중에서 찾아서( {2, 3, 5}를 곱할 수) 현재 가리키고 있는 index에서 곱해서 
       next 후보군을 갱신한다.
"""