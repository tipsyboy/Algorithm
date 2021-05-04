import sys
input = sys.stdin.readline

n = int(input())
time_table = []

# 튜플로 time table 저장
for _ in range(n):
    start, end = map(int, input().split())

    time_table.append((start, end))

time_table.sort(key=lambda x: (x[1], x[0]))  # sorting

end_time = 0  # 이전 회의가 끝나는 시간
count = 0  # 회의 수

# 회의 시간 배정하기
for start, end in time_table:
    if start >= end_time:
        end_time = end
        count += 1

print(count)


"""
    그리디 알고리즘으로 회의 끝나는 예정 시간이 빠를수록 뒷 시간에 시간 배정을 많이 할 수 있다고 생각하고 회의를 배정한다. 
    회의의 효율이나 다른 요소를 판단하지 않고 최대한 많은 회의를 수행할 수 있게 배정하기 때문에 그리디 알고리즘으로 분류할 수 있다. 
    회의의 시작시간과 종료시간이 같은 경우가 있으므로 종료시간으로 먼저 정렬을 수행하고 시작시간으로 다시 정렬을 수행한다.
"""
