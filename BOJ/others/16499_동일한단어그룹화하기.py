import sys

input = sys.stdin.readline


def solution():
    words_set = set()

    for word in words:
        temp = "".join(sorted(map(str, word)))
        words_set.add(temp)

    return len(words_set)


n = int(input())
words = []
for _ in range(n):
    word = input().rstrip()
    words.append(word)

print(solution())
