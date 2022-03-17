from heapq import heappush, heappop, heapify


def solution(jobs):
    heapify(jobs)
    length = len(jobs)
    now_time = 0
    all_running_time = 0
    waiting_q = []

    while jobs or waiting_q:
        while jobs and jobs[0][0] <= now_time:
            request, run = heappop(jobs)
            heappush(waiting_q, (run, request))

        if waiting_q:
            run, request = heappop(waiting_q)
            all_running_time += now_time - request + run
            now_time += run
        else:
            now_time += 1

    return all_running_time // length


jobs = [[0, 3], [1, 9], [2, 6]]
print(solution(jobs))