def solution(lottos, win_nums) -> list:
    ranking = [6, 6, 5, 4, 3, 2, 1]
    win_nums = set(win_nums)
    correct, erased = 0, 0

    for lotto in lottos:
        if lotto == 0:
            erased += 1
        elif lotto in win_nums:
            correct += 1

    return [ranking[correct + erased], ranking[correct]]


"""
    - rank 매기는 방식 미리 지정하고 그냥 함
"""