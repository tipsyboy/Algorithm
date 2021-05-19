import sys
input = sys.stdin.readline


# 1) sliding window
def solution1():
    # input data
    n = int(input())
    s_length = int(input())
    s = input().rstrip()
    rst = 0

    # pn 생성
    pn = "I" + "OI" * n
    pn_length = len(pn)

    # sliding window
    for i in range(s_length - pn_length):
        if pn == s[i:i + pn_length]:
            rst += 1

    return rst


# 2) "O"를 찾아 나가는 방식
def solution2():
    n = int(input())
    s_length = int(input())
    s = input().rstrip()

    count = 0  # "IOI" counter
    rst = 0  # result value
    i = 1  # index for while loop

    while i < s_length - 1:
        if s[i - 1] == "I" and s[i] == "O" and s[i + 1] == "I":
            count += 1  # pattern을 찾으면 counter 증가
            if count == n:  # pattern을 n개 만큼 찾으면,
                count -= 1  # 연속 될 수 있으니 count를 하나만 줄여주고
                rst += 1  # 결과 값 증가
            i += 1  # index++ : "OI" 때문에
        else:
            count = 0  # 패턴 못 찾은 경우 다시 시작해야 하므로 count를 0으로 줄인다.

        i += 1  # index

    return rst


# print(solution1())
print(solution2())


"""
    처음에는 슬라이딩 윈도우로 접근했지만, 결국 슬라이딩 윈도우를 하더라도 
    완전탐색의 범주에서 벗어나지 않는다. (슬라이딩 윈도우 사용해서 중간에 정답을 찾고 리턴하는 방식이 아님)
    따라서, 시간초과를 먹음..

    블로그들 찾아본 결과 pn의 기본단위인 "IOI"를 찾아서 count를 세주고 index를 늘려가는 방식으로 접근한다. 
    OI를 찾은 경우에 index 값을 두 개 증가시켜 (이미 기준 index i에서 OI를 검출했으니 2개 증가)
    다음 패턴을 찾기 시작하는 방식으로 수행양을 줄이고, pn과 s의 패턴끼리의 비교구가 없으므로 수행양이 줄어든다. 

    이런 생각은 어떻게 하는건지.. 후
"""
