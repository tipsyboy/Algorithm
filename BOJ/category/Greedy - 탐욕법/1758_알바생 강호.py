import sys

input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

arr.sort(reverse=True)
ans = 0
for i in range(N):
    if arr[i] - i <= 0:
        break
    ans += arr[i] - i

print(ans)


"""
1758. 알바생 강호
    - 0원의 팁을 받는 것보단 1원이라도 받는 것이 최적해이므로 내림차순 정렬후 최댓값을 계산하면 된다. 
    
    - 정렬 이후에 계산한 팁이 0원보다 적으면 그 이후에도 같은 결과 이므로 종료한다. 
"""