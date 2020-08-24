N = int(input())  # 입력 받을 단어의 개수

group_word = 0  # 그룹 단어의 개수 카운트

for i in range(N):
    word = input()  # 단어 입력
    flag = True  # 그룹 단어가 아닌 경우 판단

    for idx in range(len(word) - 1):
        if word[idx] == word[idx+1]:  # 알파벳 연속이 계속적으로 일어남.
            continue
        else:  # 현재 알파벳이 다음 알파벳과 다른 경우
            # 그 다음부터 끝까지 현재 알파벳을 찾아봐서 있으면,
            if word[idx+1:].find(word[idx]) != -1:
                flag = False  # flag 바꾸고 탈출
                break

    # flag가 True로 빠져나온 경우 group_word 임
    if flag == True:
        group_word += 1

print(group_word)  # 그룹 단어의 개수 세어줌
