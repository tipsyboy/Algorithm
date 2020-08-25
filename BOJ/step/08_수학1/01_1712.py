import sys

A, B, C = map(int, sys.stdin.readline().split())

# 가변비용이 판매금보다 크거나 같으면 아무리 팔아도 손해.
# 판매 대수를 x라고 할 때, (C-B)x = A 인 지점에서부터 이익이 발생.
if B >= C:
    print("-1")
else:
    print(int(A/(C-B) + 1))
