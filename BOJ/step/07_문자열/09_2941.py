# [c=, c-, dz=, d-, lj, nj, s=, z=] 만 검출하면됨

import sys
Croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
words = sys.stdin.readline()
words = words[:-1]

for c in Croatia:
    words = words.replace(c, "1")  # 위 단어가 있는 경우 '1'로 대체

print(len(words))
