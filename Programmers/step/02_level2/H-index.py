def solution(citations):
    citations.sort(reverse=True)

    for idx, value in enumerate(citations):
        if idx + 1 >= value:
            return max(idx, value)

    return len(citations)


test_case = [
    [12, 11, 10, 9, 8, 1],
    [6, 6, 6, 6, 6, 1],
    [4, 4, 4],
    [4, 4, 4, 5, 0, 1, 2, 3],
    [10, 11, 12, 13],
    [3, 0, 6, 1, 5],
    [0, 0, 1, 1],
    [0, 1],
    [10, 9, 4, 1, 1],
]

for i in range(len(test_case)):
    print(solution(test_case[i]))