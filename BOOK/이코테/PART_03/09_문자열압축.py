import sys
from heapq import heappush, heappop

input = sys.stdin.readline


def solution(s):
    length = len(s)  # 문자열 길이
    rst = length  # 최악경우 한글자도 압축이 안될 수 있으므로, rst는 문자열의 길이부터 출발한다.

    # s의 최대길이가 1000이므로 최대 500번 연산한다 - 때문에 모든 경우의 수를 전부 따진다.
    # 압축하려면 절반의 문자열은 필요하다.
    for step in range(1, length // 2 + 1):
        count = 1  # 압축 최소 수
        temp = ""  # 압축된 문자열
        compression = s[:step]  # 압축을 위한 최초 문자열

        for i in range(step, length, step):
            if compression == s[i : i + step]:  # 같은 단위만큼 문자열 검사
                count += 1  # 같으면 압축, count 증가
            else:  # 아니라면 이제 현재까지 압축한거 추가
                if count != 1:
                    temp += str(count) + compression
                else:
                    temp += compression

                compression = s[i : i + step]  # 이전 문자열을 압축 완료했으므로, 비교문자열 바꿈
                count = 1  # count 초기화

        # 남은 문자열을 추가해준다.
        if count != 1:
            temp += str(count) + compression
        else:
            temp += compression

        # 최소 압축 문자열값 갱신
        rst = min(rst, len(temp))

    return rst


# s = "aabbaccc"
# s = "ababcdcdababcdcd"
# s = "abcabcdede"
# s = "abcabcabcabcdededededede"
# s = "xababcdcdababcdcd"
# solution(s)


"""
파이썬 문자열 슬라이싱에서 문자열 범위가 넘어가는 수까지 슬라이싱을 하면 인덱스 참조 오류 나올줄 알고 예외처리 하려고 했는데,
그냥 범위 늘어나도 있는 범위까지만 참조하더라.. 그래서 그냥 했음

ex) ex_str = "aabbccdd" 하면 length가 8이고 index가 :7 까진데
    ex_str[:100] 해도 그냥 문자열 끝까지 참조하고 끝남 
"""
