import sys
from collections import deque

input = sys.stdin.readline


def sol():
    N, K = map(int, input().split())
    belt = deque(map(int, input().split()))
    robot = deque([False] * (2 * N))

    answer = 0
    while K > 0:

        # 5. 과정 카운트
        answer += 1

        # 1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전
        belt.rotate(1)
        robot.rotate(1)

        if robot[N - 1]:  # 내리는 위치에 도달함
            robot[N - 1] = False

        # 2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다.
        #  1) 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있어야 한다.
        for i in range(N - 2, -1, -1):
            if not robot[i]:  # 칸에 로봇이 없음
                continue

            # 1) 조건
            if robot[i + 1] or not belt[i + 1]:
                continue

            robot[i], robot[i + 1] = False, True
            belt[i + 1] -= 1
            if not belt[i + 1]:
                K -= 1

            if robot[N - 1]:  # 내리는 위치에 도달함
                robot[N - 1] = 0

        # 3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
        if belt[0] and not robot[0]:
            robot[0] = 1
            belt[0] -= 1
            if not belt[0]:
                K -= 1

        # # 4. 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.
        # if belt.count(0) >= K:
        #     break

    return answer


print(sol())


# ##### 2)
# import sys

# input = sys.stdin.readline


# def move_belt():
#     last = belt[2 * N - 1]
#     for i in range(2 * N - 1, 0, -1):
#         belt[i] = belt[i - 1]
#     belt[0] = last

#     for i in range(N - 1, 0, -1):
#         robot[i], robot[i - 1] = robot[i - 1], False
#     robot[N - 1] = False


# def move_robot() -> int:
#     cnt = 0
#     for i in range(N - 1, 0, -1):
#         if not robot[i - 1]:
#             continue

#         if belt[i] > 0 and not robot[i]:
#             # 이동
#             robot[i], robot[i - 1] = True, False
#             belt[i] -= 1
#             if belt[i] < 1:
#                 cnt += 1
#     robot[N - 1] = False

#     return cnt


# N, K = map(int, input().split())  # 칸, 0 기준
# belt = list(map(int, input().split()))
# robot = [False] * N

# ans = 0
# while K > 0:
#     move_belt()
#     K -= move_robot()

#     if belt[0] > 0 and not robot[0]:
#         robot[0] = True
#         belt[0] -= 1
#         if belt[0] < 1:
#             K -= 1

#     ans += 1

# print(ans)


"""
20055. 컨베이어 벨트 위의 로봇
    - 꽤 고민을 많이 했던 문제. 
      구현량은 G5~G4 정도인데 
      원래 queue라는 자료구조가 중간 값을 조회하거나 하는 따위의 행위를 할 수 없는 
      자료구조 라고 생각하면 좀 어지러워진다. 
    
    - 위의 얘기는 정의에 대한 얘기고, 파이썬에서는 가능한 일이기 때문에 1번 코드로 그냥 해결 후 
      2번 코드로 배열만 사용해서 해결했다. 
"""