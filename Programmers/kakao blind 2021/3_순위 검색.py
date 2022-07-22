from itertools import combinations


def get_table(info: list) -> dict:
    table = dict()

    for i in range(len(info)):
        parsed = info[i].split()
        parsed_info, score = parsed[:-1], int(parsed[-1])

        for j in range(5):
            for com in combinations(parsed_info, j):
                key = "".join(com)
                if key not in table:
                    table[key] = []

                table[key].append(score)

    return table


def get_cnt_valid(table: list, key: str, target_score: int) -> int:
    if key not in table:
        return 0

    scores = table[key]
    lo, hi = 0, len(scores) - 1
    ans = len(scores)
    while lo <= hi:
        mid = (lo + hi) // 2

        if scores[mid] >= target_score and (mid == 0 or scores[mid - 1] < target_score):
            ans = mid
            break
        elif scores[mid] >= target_score:
            hi = mid - 1
        else:
            lo = mid + 1

    return len(scores) - ans


def solution(info: list, query: list) -> list:
    ans = []
    table = get_table(info)

    for value in table.values():
        value.sort()

    for q in query:
        q_list = q.replace("and", "").split()
        q_list_query, target_score = q_list[:-1], int(q_list[-1])

        key = "".join(q_list_query).replace("-", "")
        ans.append(get_cnt_valid(table, key, target_score))

    return ans


"""
3. 순위 검색
    - 어떤 기준으로 문제의 난이도를 먹였는지 모르겠으나, 이게 4번보다 훨씬 어려웠다.

    - 문자열 파싱
      해쉬맵을 사용해서 쿼리에 대응하는 모든 결과를 저장하는 아이디어 / 이때, 해쉬맵의 key를 조합하는 방법
      저장된 값을 binary_search_left로 찾아내는 과정 / 이때, 미리 소팅해놓기(복잡도 개선)
      
      카카오 공식 해설을 보면 이미 3개 이상의 개념이 들어가는데 lv2... 다른 쉬운방법이 있었나?
      아니면 문자열 파싱 / 해시 맵 / 이분탐색 전부 난이도를 낮게 주는건지..
      내가 빡통인건 맞는데 lv2치고는 꽤나 어려웠다고 생각함. 
"""