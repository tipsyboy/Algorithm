
# 1
# import sys

# words = sys.stdin.readline()
# words = words[:-1].upper()  # 개행문자 지우고, 대문자 변환
# alpha_idx = [0] * 26

# for i in words:
#     alpha_idx[ord(i)-65] += 1

# if alpha_idx.count(max(alpha_idx)) > 1:
#     print("?")
# else:
#     print(chr(alpha_idx.index(max(alpha_idx))+65))

# 2 - 훨씬 빠름
import sys

words = sys.stdin.readline()
words = words[:-1].upper()  # 개행문자 지우고, 대문자 변환
words_set = set(words)
count_list = []

for i in words_set:
    count = words.count(i)
    count_list.append(count)

if count_list.count(max(count_list)) > 1:
    print("?")
else:
    max_idx = count_list.index(max(count_list))
    print(list(words_set)[max_idx])
