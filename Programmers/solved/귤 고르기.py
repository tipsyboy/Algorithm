# https://school.programmers.co.kr/learn/courses/30/lessons/138476


def solution(k, tangerine):
    tangerine_dict = dict()
    for tan in tangerine:
        tangerine_dict[tan] = tangerine_dict.get(tan, 0) + 1

    sorted_tangerine = sorted(tangerine_dict.items(), key=lambda x: x[1])
    ans = 0
    while k:
        _, cnt = sorted_tangerine.pop()
        k -= min(k, cnt)
        ans += 1

    return ans
