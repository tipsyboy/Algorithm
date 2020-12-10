def solution(numbers):
    answer = set()

    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            answer.add(numbers[i] + numbers[j])

    answer = sorted(list(answer))

    return answer


ans = solution([2, 1, 3, 4, 1])
# ans = solution([5,0,2,7])
print(ans)
