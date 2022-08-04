# # 1. set을 이용한 완전탐색
# import sys
# from itertools import combinations

# input = sys.stdin.readline


# def check_words(words: list, learned: set) -> int:
#     cnt = 0
#     for word in words:
#         flag = True
#         for i in range(len(word)):
#             if word[i] not in learned:
#                 flag = False
#                 break

#         if flag:
#             cnt += 1

#     return cnt


# def solution(words: list, N: int, K: int) -> int:
#     if K < 5:
#         return 0

#     essential = {"a", "c", "i", "n", "t"}
#     needs = set()
#     for word in words:
#         for i in range(len(word)):
#             if word[i] in essential:
#                 continue
#             needs.add(word[i])

#     ans = 0
#     if len(needs) < K - 5:
#         ans = check_words(words, essential.union(needs))
#     else:
#         for combi in combinations(list(needs), K - 5):
#             temp = essential.union(combi)
#             ans = max(ans, check_words(words, temp))

#     return ans


# N, K = map(int, input().split())
# words = []
# for _ in range(N):
#     words.append(input().rstrip())
# print(solution(words, N, K))

###########################################################################################

# 2. 비스마스킹 이용
import sys
from itertools import combinations

input = sys.stdin.readline


def get_alphabet_dict(essential: set):
    alpha = dict()
    bit = 0
    for i in range(97, 123):
        if chr(i) in essential:
            continue
        alpha[chr(i)] = bit
        bit += 1

    return alpha


def solution(words: list, N: int, K: int) -> int:
    if K < 5:
        return 0

    essential = {"a", "c", "i", "n", "t"}
    alpha = get_alphabet_dict(essential)

    word_to_bin_list = []
    for word in words:
        temp = 0
        for i in range(len(word)):
            if word[i] in essential:
                continue
            temp |= 1 << alpha[word[i]]
        word_to_bin_list.append(temp)

    pow2 = [2 ** i for i in range(21)]
    ans = 0
    for combi in combinations(pow2, K - 5):
        readable_word = 0
        for word_bin in word_to_bin_list:
            if word_bin & sum(combi) == word_bin:
                readable_word += 1

        ans = max(ans, readable_word)

    return ans


N, K = map(int, input().split())
words = []
for _ in range(N):
    words.append(input().rstrip())
print(solution(words, N, K))


"""
1062. 가르침
    0. K가 5보다 작다면 필수 알파벳조차 가르칠 수 없기 때문에, 문제에서 모든 단어를 읽을 수 없다.

    1. set을 이용한 완전탐색
    - 필수 알파벳인 {"a", "c", "i", "n", "t"}을 제외한 더 배워야 할 알파벳 중 K-5개의 모든 조합을 구해서
      모든 단어에 대입해서 읽을수 있는 최댓값을 찾아낸다. 
    
    - n의 범위가 작긴 하나 모든 단어의 모든 조합수를 완전탐색 하니 python3로는 TLE를 받았고, pypy3로 겨우 통과했다. 

    2. 비트마스킹을 이용
    - 1) 매 단어마다 필요한 필수 알파벳을 제외한 알파벳을 비트로 저장해서 합쳐 놓는다. or 연산
      예를들어, 단어에서 필요한 알파벳이 [b, d]인 경우 .....11이 될것이고 3이 저장된다. 
      
      2) 이후에 2^i (i <- 0 to 20)인 리스트를 만든다. 이 리스트는 각각의 알파벳을 의미하고 pow2라고 정의한다. (1, 2, 4, 8....)
      이제 pow2 리스트에서 K-5개를 선택한다. (알파벳을 선택하는 것)
      선택된 알파벳의 합과 1)에서 구한 단어마다의 수를 and 연산했을 때, 단어의 수와 같은 경우라면 이 단어를 읽을 수 있는 조합을 선택한 것이므로
      picked를 증가시켜준다. 

      3) 2)의 연산 결과 중 가장 큰 값이 최적해 즉, 가장 많은 단어를 읽은 경우의 수가 된다.

    
    - 하 존나게 어렵다.. 
"""