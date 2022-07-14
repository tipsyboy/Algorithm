import sys

input = sys.stdin.readline

N = int(input())
plus = []
minus = []
cnt_zero = False
for _ in range(N):
    temp = int(input())
    if temp < 0:
        minus.append(temp)
    elif temp > 0:
        plus.append(temp)
    else:
        cnt_zero = True

ans = 0
plus.sort(reverse=True)
length = len(plus)
for i in range(length // 2):
    ans += max(plus[i * 2] * plus[i * 2 + 1], plus[i * 2] + plus[i * 2 + 1])
if length % 2 != 0:
    ans += plus[length - 1]

minus.sort()
length = len(minus)
for i in range(length // 2):
    ans += minus[i * 2] * minus[i * 2 + 1]
if length % 2 != 0 and not cnt_zero:
    ans += minus[length - 1]

print(ans)


"""
1744. 수 묶기
    - 양수/음수일 때, 분기를 통해서 문제 해결

    - 1을 제외한 양수는 모두 곱했을 때가 최적 때문에, 정렬후 값이 큰 것끼리 곱해준 후 더함
      음수또한, 정렬후 절댓값이 큰 값끼리 곱해준 후에 더함. 
      이때, 음수의 개수가 홀수개일 경우 수열에 0이 존재하면 나머지 음수 하나를 0과 곱하고
      그렇지 않으면 그냥 더한다. 
"""