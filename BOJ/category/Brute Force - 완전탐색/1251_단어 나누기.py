import sys

input = sys.stdin.readline

word = input().rstrip()
ans = ""

for i in range(1, len(word) - 1):
    for j in range(i + 1, len(word)):
        temp = word[:i][::-1] + word[i:j][::-1] + word[j:][::-1]
        if not ans or temp < ans:
            ans = temp

print(ans)
