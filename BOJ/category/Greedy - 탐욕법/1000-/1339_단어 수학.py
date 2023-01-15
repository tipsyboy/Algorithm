import sys

input = sys.stdin.readline


N = int(input())
alpha = dict()
words = []
for _ in range(N):
    word = input().rstrip()
    words.append(word)
    for i in range(len(word)):
        alpha[word[i]] = alpha.get(word[i], 0) + (10 ** (len(word) - i - 1))


alpha = sorted(alpha.items(), key=lambda x: x[1], reverse=True)
num = 9
alpha_score = dict()
for i in range(len(alpha)):
    alpha_score[alpha[i][0]] = num
    num -= 1

ans = 0
for i in range(N):
    for j in range(len(words[i])):
        ans += alpha_score[words[i][j]] * (10 ** (len(words[i]) - j - 1))

print(ans)


"""
1339. 단어 수학
    - 첫 번째 방식 (WA)
      자릿수에 따라서 각각 알파벳이 갖는 최대 자릿수/최소 자릿수를 dict로 저장한 후에
      최대 자릿수를 기준으로 num을 부여하고, 같은 최대 자리수를 갖는 알파벳의 경우 최소 자릿수가 가장 큰 값을 높은 num으로 부여해서 풀었다. 
      but, 아래의 반례에 막혔음.

    - 두 번째 방식 (AC)
    알파벳의 자릿수에 대해서 점수를 준다는 아이디어는 동일하나, 단순 자리의 위치만이 아닌 자릿수 그 자체에서 수가 나타내는 크기에 대해 가중치?를 할당함
    위의 할당된 점수를 가지고 각각의 알파벳에 num을 부여하고, 이것을 바탕으로 결과 값을 냄

    꽤나, 어지러운 문제였음. 확실히 그리디한 방식은 난이도가 올라 갈수록 확연하게 어려워지는 것 같다.
"""


"""
- 반례

10
ABB
BB
BB
BB
BB
BB
BB
BB
BB
BB
"""