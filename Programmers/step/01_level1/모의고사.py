def solution(answers):
    winner = []
    num_q = len(answers)

    # 수포자 패턴
    supo_1 = [1, 2, 3, 4, 5]
    supo_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supo_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    score = [0, 0, 0]  # 점수

    for i in range(num_q):
        if answers[i] == supo_1[i % len(supo_1)]:
            score[0] += 1

        if answers[i] == supo_2[i % len(supo_2)]:
            score[1] += 1

        if answers[i] == supo_3[i % len(supo_3)]:
            score[2] += 1

    for person, s in enumerate(score):
        if s == max(score):
            winner.append(person + 1)

    return winner


# print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 2, 4, 2]))
