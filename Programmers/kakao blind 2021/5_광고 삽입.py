# https://school.programmers.co.kr/learn/courses/30/lessons/72414


def convert_time_hours_to_seconds(hours: str) -> int:
    hours = hours.split(":")

    return int(hours[0]) * 3600 + int(hours[1]) * 60 + int(hours[2])


def convert_time_seconds_to_hours(time: int) -> str:
    hours = time // 3600
    time = time % 3600
    minutes = time // 60
    seconds = time % 60

    hours = "0" + str(hours) if hours < 10 else str(hours)
    minutes = "0" + str(minutes) if minutes < 10 else str(minutes)
    seconds = "0" + str(seconds) if seconds < 10 else str(seconds)

    return hours + ":" + minutes + ":" + seconds


def solution(play_time: str, adv_time: str, logs: list) -> str:
    # 1. 시간을 전부 초단위로 바꿈
    play_end = convert_time_hours_to_seconds(play_time)
    adv_time = convert_time_hours_to_seconds(adv_time)
    all_play_time = [0] * (play_end + 1)
    for log in logs:
        log = log.split("-")
        s = convert_time_hours_to_seconds(log[0])
        e = convert_time_hours_to_seconds(log[1])
        all_play_time[s] += 1
        all_play_time[e] += -1

    # 2. 해당 시간(s)에서 보고 있는 시청자 수
    #  ex) a[3] = 2 -> 3s에서 2명의 시청자가 보고 있었음
    for i in range(1, play_end + 1):
        all_play_time[i] = all_play_time[i - 1] + all_play_time[i]

    # 3. 해당 시간(s)에서 누적 시청 시간의 누적 합
    #  ex) i=10 -> 10s까지 시청자들이 본 시간의 총 합
    for i in range(1, play_end + 1):
        all_play_time[i] = all_play_time[i - 1] + all_play_time[i]

    max_view = all_play_time[adv_time - 1]
    time = 0
    for i in range(adv_time, play_end + 1):
        if max_view < all_play_time[i] - all_play_time[i - adv_time]:
            max_view = all_play_time[i] - all_play_time[i - adv_time]
            time = i - adv_time + 1

    return convert_time_seconds_to_hours(time)


def solution2(play_time: str, adv_time: str, logs: list) -> str:
    # 1. 시간을 전부 초단위로 바꿈
    play_end = convert_time_hours_to_seconds(play_time)
    adv_time = convert_time_hours_to_seconds(adv_time)
    watching_num = [0] * (play_end + 1)
    for log in logs:
        log = log.split("-")
        s = convert_time_hours_to_seconds(log[0])
        e = convert_time_hours_to_seconds(log[1])
        watching_num[s] += 1
        watching_num[e] += -1

    # 2. 해당 시간(s)에서 보고 있는 시청자 수
    #  ex) w[3] = 2 -> 3s에서 2명의 시청자가 보고 있었음
    for i in range(1, play_end + 1):
        watching_num[i] = watching_num[i - 1] + watching_num[i]

    max_view = sum(watching_num[:adv_time])
    adv_start_time = 0
    now = max_view
    for i in range(1, play_end - adv_time + 2):
        now = now - watching_num[i - 1] + watching_num[i + adv_time - 1]
        if max_view < now:
            max_view = now
            adv_start_time = i

    return convert_time_seconds_to_hours(adv_start_time)


play_time = "00:00:15"
adv_time = "00:00:05"
logs = ["00:00:02-00:00:04", "00:00:03-00:00:08", "00:00:09-00:00:11", "00:00:09-00:00:13", "00:00:07-00:00:08"]
solution(play_time, adv_time, logs)
