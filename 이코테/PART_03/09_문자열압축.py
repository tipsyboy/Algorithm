def solution(s):
    # 예외처리
    if len(s) == 1:
        return 1

    rst = []
    for step in range(1, len(s)//2 + 1):
        temp = s[:step]  # 문자열 처음 비교 구
        count = 1  # 압축 문자열 count
        compressed_str = ""  # 압축된 문자열

        for i in range(step, len(s), step):
            if temp == s[i:i+step]:
                count += 1
            else:
                if count == 1:  # count가 1이면 생략한다.
                    compressed_str += temp
                else:
                    compressed_str += str(count) + temp  # 압축된 문자열을 넣고
                count = 1  # 다시 count = 1
                temp = s[i:i+step]  # 새로운 temp 비교 구

        # 나머지 문자열 추가
        if count == 1:
            compressed_str += temp
        else:
            compressed_str += str(count) + temp

        # print(compressed_str)
        rst.append(len(compressed_str))

    return min(rst)


input_str = input()
# input_str = "aabbccdd"
print(solution(input_str))

"""
파이썬 문자열 슬라이싱에서 문자열 범위가 넘어가는 수까지 슬라이싱을 하면 인덱스 참조 오류 나올줄 알고 예외처리 하려고 했는데,
그냥 범위 늘어나도 있는 범위까지만 참조하더라.. 그래서 그냥 했음

ex) ex_str = "aabbccdd" 하면 length가 8이고 index가 :7 까진데
    ex_str[:100] 해도 그냥 문자열 끝까지 참조하고 끝남 
"""
