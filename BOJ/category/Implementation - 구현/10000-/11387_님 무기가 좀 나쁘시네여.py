# 2024.08.08 THU
# https://www.acmicpc.net/problem/11387

import sys

input = sys.stdin.readline


def equip(character, weapon):
    stats = []
    for stat, w in zip(character, weapon):
        stats.append(stat + w)
    atk, strength, cri_per, cri_dmg_rate, ats = stats

    return atk * (100 + strength) * (100 * (100 - min(cri_per, 100)) + min(cri_per, 100) * cri_dmg_rate) * (100 + ats)


def diff(character, og_weapon, change_weapon):
    if equip(character, og_weapon) < equip(character, change_weapon):
        return "+"

    if equip(character, og_weapon) > equip(character, change_weapon):
        return "-"

    return "0"


kriii = list(map(int, input().split()))
pabu = list(map(int, input().split()))
w1 = list(map(int, input().split()))
w2 = list(map(int, input().split()))

for i in range(5):
    kriii[i] = kriii[i] - w1[i]
    pabu[i] = pabu[i] - w2[i]

print(diff(kriii, w1, w2))
print(diff(pabu, w2, w1))
