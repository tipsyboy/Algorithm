# https://school.programmers.co.kr/learn/courses/30/lessons/250135


def time_to_seconds(hour, minutes, seconds):
    return hour * 3600 + minutes * 60 + seconds


def solution(h1, m1, s1, h2, m2, s2):
    cur_time = time_to_seconds(h1, m1, s1)
    end_time = time_to_seconds(h2, m2, s2)

    ans = 0
    if cur_time == 0 or cur_time == 12 * 60 * 60:
        ans += 1

    h_degree = cur_time / 120 % 360
    m_degree = cur_time / 10 % 360
    s_degree = cur_time * 6 % 360
    while cur_time < end_time:
        nxt_h = 360 if (cur_time + 1) / 120 % 360 == 0 else (cur_time + 1) / 120 % 360
        nxt_m = 360 if (cur_time + 1) / 10 % 360 == 0 else (cur_time + 1) / 10 % 360
        nxt_s = 360 if (cur_time + 1) * 6 % 360 == 0 else (cur_time + 1) * 6 % 360

        if s_degree < h_degree and nxt_s >= nxt_h:
            ans += 1
        if s_degree < m_degree and nxt_s >= nxt_m:
            ans += 1
        if nxt_h == nxt_m == nxt_s:
            ans -= 1

        h_degree = 0 if nxt_h == 360 else nxt_h
        m_degree = 0 if nxt_m == 360 else nxt_m
        s_degree = 0 if nxt_s == 360 else nxt_s
        cur_time += 1

    return ans
