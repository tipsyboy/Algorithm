# https://school.programmers.co.kr/learn/courses/30/lessons/250137


def solution(bandage, health, attacks):
    casting, per_second, bonus = bandage
    cur_health = health
    prev = 0
    for time, damage in attacks:
        passed = time - prev - 1
        success = passed // casting
        cur_health = min(health, cur_health + passed * per_second + bonus * success)
        prev = time

        cur_health -= damage
        if cur_health < 1:
            return -1
    return cur_health


print(solution([5, 1, 5], 30, [[2, 10], [9, 15], [10, 5], [11, 5]]))
print(solution([3, 2, 7], 20, [[1, 15], [5, 16], [8, 6]]))
print(solution([4, 2, 7], 20, [[1, 15], [5, 16], [8, 6]]))
print(solution([1, 1, 1], 5, [[1, 2], [3, 2]]))
