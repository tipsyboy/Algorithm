# n번째 계단까지 오를때 최댓값을 f(n)이라고 하고, n번째 계단의 점수를 s(n)이라고 하면
# n번째 계단까지 오를때, n-1을 밟는 경우가 있고 n-2를 밟는 경우의 수 두가지가 있다.
# 왜냐하면 연속적인 세 계단은 밟을 수 없기 때문   즉,
# f(1) = s(1)
# f(2) = s(1) + s(2)
# f(3) = s(1) + s(3) or s(1) + s(3) -> n번째 계단은 무조건 밟아야 한다.
# f(4) = s(4) + s(3) + f(1)   or  s(4) + f(2)
# f(5) = s(5) + s(4) + f(2)   or  s(5) + f(3)
# f(6) = s(6) + s(5) + f(3)   or  s(6) + f(4)
#                   ...
# f(n) = s(n) + s(n-1) + f(n-3) or s(n) + f(n-2)


import sys


def go_up_stair(n):
    stair_score = []

    for i in range(n):
        stair_score.append(int(sys.stdin.readline()))

    max_score = []

    if n == 1:
        return stair_score[0]
    if n == 2:
        return stair_score[0] + stair_score[1]

    max_score.append(stair_score[0])
    max_score.append(stair_score[0] + stair_score[1])
    max_score.append(max(stair_score[2] + stair_score[0],
                         stair_score[2] + stair_score[1]))

    for i in range(3, n):
        max_score.append(max(stair_score[i] + stair_score[i-1] + max_score[i-3],
                             stair_score[i] + max_score[i-2]))

    return max_score[-1]


n = int(sys.stdin.readline())
print(go_up_stair(n))
