# https://school.programmers.co.kr/learn/courses/30/lessons/250137


def solution(bandage, health, attacks):
    attacks.sort(reverse=True)
    t, h, b = bandage  # 시전 시간, 초당 회복량, 추가 회복량
    cur_health = health
    time = 0
    success = 0
    while attacks:
        time += 1

        if time == attacks[-1][0]:
            _, damage = attacks.pop()  # 공격 시간, 피해량
            cur_health -= damage
            success = 0
            if cur_health < 1:
                return -1
            continue

        cur_health = min(health, cur_health + h)
        success += 1
        if success == t:
            cur_health = min(health, cur_health + b)
            success = 0

    return cur_health


print(solution([5, 1, 5], 30, [[2, 10], [9, 15], [10, 5], [11, 5]]))
print(solution([3, 2, 7], 20, [[1, 15], [5, 16], [8, 6]]))
print(solution([4, 2, 7], 20, [[1, 15], [5, 16], [8, 6]]))
print(solution([1, 1, 1], 5, [[1, 2], [3, 2]]))
