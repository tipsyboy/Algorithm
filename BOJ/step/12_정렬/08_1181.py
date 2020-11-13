import sys

n = int(sys.stdin.readline())

words = []

for i in range(n):
    words.append(sys.stdin.readline().strip())

words = list(set(words))  # 중복 제거

words.sort(key=lambda x: (len(x), x))  # 정렬: 길이 기준->사전순서

# for word in words:
#     print(word)

print("\n".join(words))  # words를 합쳐서 출력한다. 각 원소를 \n로 엮어서
