# https://www.acmicpc.net/problem/2036

"""
2036. 수열의 점수
    - 중간에 문제 이해가 꼬여서 삽질할뻔

    - 양수 / 음수 / 0 으로 나누고 정렬해서 각각 차례에 액션중 이득이 되는 행위만 하면됨
    
    - 이렇게 정렬된 각각의 원소들에서
      양수의 경우 두 수를 뽑아 하나 이상 1인 경우에 더하는 것이 이득이고 / 아니라면 곱해야 이득
      음수는 두 수를 곱해서 양수로 만들어주고 남은 수는 0을 곱해 0으로 만들어주거나 0이 없는 경우에 그냥 더한다.
      

8
1   
1
1
5
-1
-2
-3
0
"""
import sys

input = sys.stdin.readline

n = int(input())

plus, minus, zero = [], [], 0
for _ in range(n):
    elem = int(input())
    if elem == 0:
        zero += 1
    elif elem > 0:
        plus.append(elem)
    else:
        minus.append(elem)

plus.sort()
minus.sort(reverse=True)

ans = 0
for _ in range(len(plus) // 2):
    f, s = plus.pop(), plus.pop()
    if f == 1 or s == 1:
        ans += f + s
    else:
        ans += f * s
if plus:
    ans += plus.pop()

for _ in range(len(minus) // 2):
    ans += minus.pop() * minus.pop()

if minus and not zero:
    ans += minus.pop()

print(ans)
