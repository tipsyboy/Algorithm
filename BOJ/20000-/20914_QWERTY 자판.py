# 2024.11.14 THU
# https://www.acmicpc.net/problem/20914

import sys

input = sys.stdin.readline
INF = float("inf")


keyboard = {
    # 첫 번째 행
    "Q": ["W", "A"],
    "W": ["Q", "E", "A", "S"],
    "E": ["W", "R", "S", "D"],
    "R": ["E", "T", "D", "F"],
    "T": ["R", "Y", "F", "G"],
    "Y": ["T", "U", "G", "H"],
    "U": ["Y", "I", "H", "J"],
    "I": ["U", "O", "J", "K"],
    "O": ["I", "P", "K", "L"],
    "P": ["O", "L"],
    # 두 번째 행
    "A": ["Q", "W", "S", "Z"],
    "S": ["W", "E", "A", "D", "Z", "X"],
    "D": ["E", "R", "S", "F", "X", "C"],
    "F": ["R", "T", "D", "G", "C", "V"],
    "G": ["T", "Y", "F", "H", "V", "B"],
    "H": ["Y", "U", "G", "J", "B", "N"],
    "J": ["U", "I", "H", "K", "N", "M"],
    "K": ["I", "O", "J", "L", "M"],
    "L": ["O", "P", "K"],
    # 세 번째 행
    "Z": ["A", "S", "X"],
    "X": ["S", "D", "Z", "C"],
    "C": ["D", "F", "X", "V"],
    "V": ["F", "G", "C", "B"],
    "B": ["G", "H", "V", "N"],
    "N": ["H", "J", "B", "M"],
    "M": ["J", "K", "N"],
}

dist = [[INF] * 26 for _ in range(26)]
for i in range(26):
    dist[i][i] = 0

for k, values in keyboard.items():
    x = ord(k) - 65
    for y in values:
        y = ord(y) - 65
        dist[x][y] = 1
        dist[y][x] = 1

for k in range(26):
    for p in range(26):
        for q in range(26):
            if dist[p][q] > dist[p][k] + dist[k][q]:
                dist[p][q] = dist[p][k] + dist[k][q]


N = int(input())
for _ in range(N):
    word = input().rstrip()
    m = len(word)
    # ㅇ니ㅏ렁ㅁ니라ㅓㅇㄴ리ㅏ;언ㅁㄹ 아하기싫어
    cnt = 0
    for i in range(m - 1):
        cnt += dist[ord(word[i]) - 65][ord(word[i + 1]) - 65]
    print(cnt * 2 + m)
