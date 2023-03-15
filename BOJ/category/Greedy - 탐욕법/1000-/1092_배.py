# https://www.acmicpc.net/problem/1092

import sys

input = sys.stdin.readline


def solve1(cranes: list, boxes: list) -> int:
    cranes = sorted(cranes, reverse=True)
    boxes = sorted(boxes, reverse=True)

    if cranes[0] < boxes[0]:
        return -1

    ans = 0
    carried = set()
    while len(carried) < M:
        idx = 0
        for crane in cranes:
            while idx < M:
                if idx in carried:
                    idx += 1
                    continue
                if crane >= boxes[idx]:
                    carried.add(idx)
                    idx += 1
                    break
                idx += 1
        ans += 1

    return ans


def solve2(cranes: list, boxes: list) -> int:
    cranes = sorted(cranes, reverse=True)
    boxes = sorted(boxes, reverse=True)

    if cranes[0] < boxes[0]:
        return -1

    assigned = [0] * N
    for box in boxes:
        target, temp = 0, assigned[0]
        for i in range(N):
            if box > cranes[i]:
                break
            # 더 작은 크레인이 옮길 수 있으면서
            if assigned[i] <= temp:  # 할당 된 작업도 적은 경우
                target = i
                temp = assigned[i]

        assigned[target] += 1  # target 크레인에 작업을 할당함

    return max(assigned)


N = int(input())
cranes = list(map(int, input().split()))
M = int(input())
boxes = list(map(int, input().split()))

print(solve1(cranes, boxes))
print(solve2(cranes, boxes))


"""
1092. 배
    - i번 박스를 bi라고 할때, bi를 옮길 수 있는 매분마다 bi를 옮길 수 있는 가장 작은 크레인으로 옮겨야 한다. 
    
    0. 위의 코드에는 없지만, 박스를 전부 옮길때까지 매 번 현재 크레인이 옮길 수 있는 가장 큰 박스를 옮기는 방향으로 3중 루프를 돌면서 선택 된 박스를 지웠다. 
       3중루프에 원소 삭제시 배열 재배치도 수시로 일어나면서 몹시 비효율적이지만, 문제에 주어진 범위가 작기 때문에 마지널하게 통과 할 수 있다고 생각했고 pypy로 통과했다. (python3는 TLE)
    
    1. solve1() 해결법 - 0번과 같은 방식이지만, 옮긴 박스를 set()으로 처리하면서 위의 배열 재배치 문제만 해결함
       python3로는 여전히 TLE지만 pypy로 2000ms 정도 줄일 수 있었다. 그래도 0, 1 번 풀이는 정해는 아닐듯
    
    2. 각각 크레인에 할당 된 작업량을 나타내는 assigned[]를 두고 bi를 옮길 수 있는 가장 작은 크레인을 찾아내는 방식
       최초 정의한 그리디한 방식에 가장 부합한 풀이인듯.?
"""