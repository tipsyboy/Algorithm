# # 비고- 존나틀림;; 사ㅣㅂ리

# import sys

# input = sys.stdin.readline

# n = int(input())
# words = [[0] * 26 for _ in range(n)]
# for i in range(n):
#     string = input().rstrip()
#     for s in string:
#         words[i][ord(s) - ord("A")] += 1

# rst = 0
# for word in words[1:]:
#     p, m = 0, 0
#     for i in range(26):
#         if word[i] > words[0][i]:
#             p += word[i] - words[0][i]
#         else:
#             m += words[0][i] - word[i]
#     if p < 2 and m < 2:
#         rst += 1

# print(rst)


import sys

input = sys.stdin.readline


def get_alpha_in_word(word) -> list:
    alpha = [0] * 26
    for i in range(len(word)):
        alpha[ord(word[i]) - 65] += 1

    return alpha


N = int(input())
f_word = input().rstrip()
first = get_alpha_in_word(f_word)

ans = 0
for _ in range(N - 1):
    word = input().rstrip()
    alpha = get_alpha_in_word(word)

    plus, minus = 0, 0
    for i in range(26):
        if first[i] < alpha[i]:
            plus += alpha[i] - first[i]
        else:
            minus += first[i] - alpha[i]

    if plus < 2 and minus < 2:
        ans += 1
print(ans)


"""
2607. 비슷한 단어
    - 실3 인데 굉장히 애먹었음....

    - 첫 번째 단어와 이후 단어들을 비교해서 부족하면 더해주고 남으면 빼주는 방식
"""