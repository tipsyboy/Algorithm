# https://school.programmers.co.kr/learn/courses/30/lessons/340212


def solution(diffs, times, limit):
    lo, hi = 1, max(diffs)

    ans = -1
    while lo <= hi:
        level = (lo + hi) // 2

        rst = 0
        for idx, (diff, time) in enumerate(zip(diffs, times)):
            if diff <= level:
                rst += time
            else:
                rst += (diff - level) * (times[idx - 1] + time) + time

        if rst <= limit:
            ans = level
            hi = level - 1
        else:
            lo = level + 1

    return ans


print(solution([1, 5, 3], [2, 4, 7], 30))  # 3
print(solution([1, 4, 4, 2], [6, 3, 8, 2], 59))  # 2
print(solution([1, 328, 467, 209, 54], [2, 7, 1, 4, 3], 1723))  # 294
print(solution([1, 99999, 100000, 99995], [9999, 9001, 9999, 9001], 3456789012))  # 39354
