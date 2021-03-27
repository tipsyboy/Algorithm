import sys

input = sys.stdin.readline
n = int(input())

words = set()
for _ in range(n):
    words.add(input().rstrip())

words = list(words)

words = sorted(words, key=lambda x: (len(x), x))

# for word in words:
#     print(word)

print("\n".join(words))
