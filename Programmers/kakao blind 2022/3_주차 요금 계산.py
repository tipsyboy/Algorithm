def cal_fee(time, fees) -> int:
    if time <= fees[0]:
        return fees[1]
    else:
        over_time = (time - fees[0]) // fees[2]
        if (time - fees[0]) % fees[2]:
            over_time += 1

        return over_time * fees[3] + fees[1]


def cal_parking_time(in_time, out_time) -> int:
    in_hour, in_minutes = in_time.split(":")
    in_time = int(in_hour) * 60 + int(in_minutes)
    out_hour, out_minutes = out_time.split(":")
    out_time = int(out_hour) * 60 + int(out_minutes)

    return out_time - in_time


def solution(fees, records) -> list:
    # 출차 기록이 없다면 23:59에 출차 간주
    # [기본 시간] 이하 -> [기본 요금] 청구
    # [기본 시간] 초과 -> [기본 요금] + [단위 시간] * [단위 요금] (올림)
    # 결과 리턴은 [차량 번호] 오름차순
    # 주차 요금은 한꺼번에 정산한다 *******

    # 1. 입출차 시간 계산
    PARKING_TIME = dict()  # 주차 시간 누적
    IN = dict()  # 입차 시간
    for record in records:
        time, number, command = record.split()
        if command == "IN":
            IN[number] = time
            if number not in PARKING_TIME:
                PARKING_TIME[number] = 0

        elif command == "OUT":
            PARKING_TIME[number] += cal_parking_time(IN[number], time)
            IN.pop(number)

    # 2. 23:59이후 출차 간주 일괄 계산
    for number, time in IN.items():
        PARKING_TIME[number] += cal_parking_time(IN[number], "23:59")

    # 3. 차량 번호 오름차순
    rst = []
    for number in sorted(PARKING_TIME.keys()):
        rst.append(cal_fee(PARKING_TIME[number], fees))

    return rst


fees = [180, 5000, 10, 600]  # 기본 시간, 기본 요금, 단위 시간, 단위 요금
records = [
    "05:34 5961 IN",
    "06:00 0000 IN",
    "06:34 0000 OUT",
    "07:59 5961 OUT",
    "07:59 0148 IN",
    "18:59 0000 IN",
    "19:09 0148 OUT",
    "22:59 5961 IN",
    "23:00 5961 OUT",
]


print(solution(fees, records))