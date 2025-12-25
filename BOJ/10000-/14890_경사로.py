import sys

input = sys.stdin.readline


def set_ramp(road) -> bool:
    setted_ramp = [False] * len(road)  # setted_ramp[x]: x의 위치에 경사로가 설치되었는가?
    idx = 0  # 길 위치 index

    while idx < len(road) - 1:
        diff = abs(road[idx] - road[idx + 1])  # 인접 위치의 높이 차이

        # 1. 인접 위치의 높이가 1보다 높은 경우
        if diff > 1:
            return False

        # 2. 인접 위치의 높이가 0인 경우
        if diff == 0:
            idx += 1  # 인접위치의 높이차가 없으므로 이미 지나갈 수 있는 길이다.
            continue

        # 3. 인접 위치의 높이가 1이다.
        if road[idx] > road[idx + 1]:  # 높은 곳 -> 낮은 곳
            if idx + L > len(road) - 1:  # OOB
                return False

            for i in range(idx + 1, idx + L + 1):
                if setted_ramp[i] or road[idx + 1] != road[i]:  # 경사로를 설치할 수 없다.
                    return False
                setted_ramp[i] = True  # 경사로 설치
            idx += L  # 위치 조정
        else:  # 낲은 곳 -> 높은 곳
            if idx - L + 1 < 0:  # OOB
                return False

            for i in range(idx, idx - L, -1):
                if setted_ramp[i] or road[idx] != road[i]:
                    return False
                setted_ramp[i] = True
            idx += 1

    return True


N, L = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

cnt = 0  # result answer
# 가로 방향 검사
for i in range(N):
    if set_ramp(graph[i]):
        cnt += 1

# 세로방향 검사
col_graph = list(zip(*graph))
for i in range(N):
    if set_ramp(col_graph[i]):
        cnt += 1

print(cnt)

"""
    14890. 경사로 

    - set_ramp() 함수를 만들어 경로가 될 수 있는지/없는지만 반환하고, 각 행/열을 돌면서 가능한 경사로를 찾아낸다. 

    - 문제의 조건에 맞게 구현만 하면 되는 문제지만, 역량테스트 특성상 좀 복잡했다. (티어가 말해주듯 다른 문제에 비해서는 간단했던거 같긴함)
    
    - 각각의 위치를 탐색하면서 길이 될수 없는 부분에 초점을 맞춰서 구현했다. 
      1. 인접 위치의 높이 차가 1초과인 경우
      2. 인접 위치의 차가 없는 경우 (이미 길이 형성됨)
      3. 각각의 길마다 이미 설치 된 경사로 배열(setted_ramp[])을 따로 설정해 이미 경사로가 설치된 부분이 중복되면 실패하는 경우 
"""