# https://school.programmers.co.kr/learn/courses/30/lessons/340213


def time_to_seconds(time):
    minutes, seconds = map(int, time.split(":"))
    return minutes * 60 + seconds


def seconds_to_time(sec_time):
    minutes, seconds = map(str, divmod(sec_time, 60))
    return minutes.zfill(2) + ":" + seconds.zfill(2)


def is_opening(sec, op_start_sec, op_end_sec):
    if op_start_sec <= sec <= op_end_sec:
        return True
    return False


def solution(video_len, pos, op_start, op_end, commands):
    video_len_sec = time_to_seconds(video_len)
    cur = time_to_seconds(pos)
    op_start_sec = time_to_seconds(op_start)
    op_end_sec = time_to_seconds(op_end)

    if op_start_sec <= cur <= op_end_sec:
        cur = op_end_sec

    for command in commands:
        if command == "prev":
            cur = max(0, cur - 10)
        elif command == "next":
            cur = min(video_len_sec, cur + 10)

        if op_start_sec <= cur <= op_end_sec:
            cur = op_end_sec

    return seconds_to_time(cur)


print(solution("34:33", "13:00", "00:55", "02:55", ["next", "prev"]))
print(solution("10:55", "00:05", "00:15", "06:55", ["prev", "next", "next"]))
print(solution("07:22", "04:05", "00:15", "04:07", ["next"]))


"""
동영상 재생기

- 시간 문제는 초로 변경 하는 것이 편함
- 처음 현재 시간에서 오프닝 시간인지 확인하고 변경 시켜야함
"""
