# def solution(n, stages):
#     fail_rate = dict()
#     length = len(stages)

#     for i in range(1, n + 1):
#         count = stages.count(i)

#         if length == 0:
#             fail_rate[i] = 0
#         else:
#             fail_rate[i] = count / length
#             length -= count

#     fail_rate = sorted(fail_rate.items(), key=lambda x: -x[1])
#     fail_rate = [x[0] for x in fail_rate]
#     print(fail_rate)

#     return fail_rate


def solution(n, stages):
    fail_rate = dict()
    length = len(stages)

    # init dict
    for i in range(1, n + 1):
        fail_rate[i] = 0

    for stage in stages:
        if stage > n:
            continue
        fail_rate[stage] += 1

    for i in range(1, n + 1):

        if length == 0:
            fail_rate[i] = 0
        else:
            temp = fail_rate[i]
            fail_rate[i] = temp / length
            length -= temp

    # print(fail_rate)
    fail_rate = sorted(fail_rate.items(), key=lambda x: -x[1])
    fail_rate = [x[0] for x in fail_rate]
    print(fail_rate)

    return fail_rate


solution(5, [2, 1, 2, 6, 2, 4, 3, 3])
# solution(4, [4, 4, 4, 4])
