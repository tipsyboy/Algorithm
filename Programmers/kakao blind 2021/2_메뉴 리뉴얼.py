from itertools import combinations


def get_cadidates(orders: list, menu_cnt: int) -> list:
    candidates = []
    for order in orders:
        if len(order) < menu_cnt:
            continue
        for combination in combinations(sorted(order), menu_cnt):
            candidates.append("".join(combination))

    return candidates


def solution(orders: list, course: list) -> list:
    ans = []

    for menu_cnt in course:
        # 1.
        candidates = get_cadidates(orders, menu_cnt)

        # 2.
        set_menu_dict = dict()
        for candidate in candidates:
            set_menu_dict[candidate] = set_menu_dict.get(candidate, 0) + 1

        if not set_menu_dict:
            continue

        set_menu = sorted(set_menu_dict.items(), key=lambda x: -x[1])
        prev = set_menu[0][1]
        for combi, cnt in set_menu:
            if cnt < 2 or prev != cnt:
                break

            ans.append(combi)

    # 3
    return sorted(ans)


"""
    메뉴 리뉴얼

    1. 세트 메뉴의 요리의 개수마다 각 주문에서 나올 수 있는 세트 메뉴를 확인

    2. 유효성 검사 및 가장 많은 조합을 세트메뉴로 채택한다.

    3. 소팅후 리턴
"""