def solution(clothes):
    tag = dict()

    for i in range(len(clothes)):
        tag[clothes[i][1]] = tag.get(clothes[i][1], 0) + 1

    rst = 1
    for name, num in tag.items():
        rst *= num + 1

    return rst - 1


clothes = [
    ["yellowhat", "headgear"],
    ["bluesunglasses", "eyewear"],
    ["green_turban", "headgear"],
]
solution(clothes)