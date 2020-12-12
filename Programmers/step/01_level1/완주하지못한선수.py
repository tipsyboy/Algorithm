
# ### 1. 첫번째 풀이
# def solution(participant, completion):
#     participant.sort()
#     completion.sort()

#     for i in range(len(completion)):
#         if participant[i] != completion[i]:
#             return participant[i]

#     return participant[i+1]

# 2. collections 모듈의 Counter 클래스 사용
import collections


def solution(participant, completion):
    temp = collections.Counter(participant) - collections.Counter(completion)

    answer = list(temp.keys())[0]

    return answer


x = solution(["leo", "kiki", "eden"],
             ["eden", "kiki"])

y = solution(["marina", "josipa", "nikola", "vinko", "filipa"],
             ["josipa", "filipa", "marina", "nikola"])
z = solution(["mislav", "stanko", "mislav", "ana"],
             ["stanko", "ana", "mislav"])

# print(x, y, z)
