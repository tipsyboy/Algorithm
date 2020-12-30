def solution(array, commands):
    answer = []

    for idx, command in enumerate(commands):
        start = command[0] - 1
        end = command[1]
        k = command[2] - 1

        temp = sorted(array[start:end])
        answer.append(temp[k])

    return answer


def solution_2(array, commands):
    answer = []

    for command in commands:
        start, end, k = command

        answer.append(sorted(array[start - 1 : end])[k - 1])

    return answer


# def solution_3(array, commands):
#     t = list(map(lambda x: sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
#     print(t)


solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 4]])
