from collections import Counter
from itertools import combinations


def solution(orders: list, course: list) -> list:
    ans = []

    for menu_cnt in course:
        candidates = []
        for order in orders:
            candidates += combinations(sorted(order), menu_cnt)
        candidates = sorted(Counter(candidates).items(), key=lambda x: -x[1])

        if not candidates:
            continue

        most_ordered_cnt = candidates[0][1]
        for candidate, cnt in candidates:
            if cnt < 2 or cnt < most_ordered_cnt:
                break
            ans.append("".join(candidate))

    return sorted(ans)


orders = ["XYZ", "XWY", "WXA"]
course = [2, 3, 4]
solution(orders, course)


"""
    - Counter를 써봤음.
"""