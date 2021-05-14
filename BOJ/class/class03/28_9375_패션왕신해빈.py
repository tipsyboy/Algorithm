import sys
input = sys.stdin.readline


def get_wear_com(n):
    type_count = dict()
    rst = 1  # 결과 값

    for _ in range(n):
        w_name, w_type = input().split()  # 옷의 종류 입력 받기

        # dict에 key가 있는 경우 count를 증가시키고 없으면 추가한다.
        if type_count.get(w_type):
            type_count[w_type] += 1
        else:
            type_count[w_type] = 1

    # 조합 계산
    for item in type_count.values():
        rst *= item + 1

    # 해빈이가 알몸으로 다니는 경우의 수를 하나 빼준 값을 리턴한다.
    return rst - 1


# main
t = int(input())  # test case
for _ in range(t):
    n = int(input())  # 해빈이가 가지고 있는 의상의 수

    print(get_wear_com(n))
