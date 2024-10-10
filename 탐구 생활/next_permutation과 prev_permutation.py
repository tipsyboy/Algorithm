"""
# Last Modified. 2024.10.10 THU
# 다음 순열(next_permutation)과 이전 순열(prev_permutation)

# ref. https://alinghi.tistory.com/3

    next_permutation 기준으로 prev의 경우는 반대로 생각하면 된다. 

    1. 순열의 첫 번째는 모든 원소가 오름차순이다.

    2. 순열의 마지막 번째는 모든 원소가 내림차순이다. 
    
    3. 뒤에서부터 탐색하면서 모두 내림차순인 부분순열을 찾는다. 
      -> 부분순열이 전체수열이 아닌 경우는 다음 순열이 있다는 뜻이며, 이것은 내림차순으로 갈 수 있다는 말
      -> 즉, 마지막 순열이 아니라는 뜻임.

    4. 부분 순열 바로 앞의 원소보다 큰 가장 작은 원소를 찾는다. 

    5. 4.교체후 부분 순열을 뒤집어준다. 
      왜why?-> 4.의 경우를 함께 살펴 봤을때 부분순열은 모두 내림차순이었으므로 이 다음순열을 찾기 위해선 부분순열이 다시 오름차순을 가져야한다.
      그런데 교체된 원소를 기준으로 우측은 작은 원소 / 좌측은 큰 원소가 위치하는 것이 자명하므로 
      부분 순열을 뒤집어서 오름차순으로 만든다.
"""


def next_permutation(arr: list) -> bool:
    length = len(arr)

    for p in range(length - 1, 0, -1):
        if arr[p - 1] >= arr[p]:
            continue

        for q in range(length - 1, 0, -1):
            if arr[p - 1] >= arr[q]:
                continue

            arr[p - 1], arr[q] = arr[q], arr[p - 1]
            r = length - 1
            while p < r:
                arr[p], arr[r] = arr[r], arr[p]
                p += 1
                r -= 1

            return True

    return False


def prev_permutation(arr: list) -> bool:
    length = len(arr)

    for p in range(length - 1, 0, -1):
        if arr[p - 1] <= arr[p]:
            continue

        for q in range(length - 1, 0, -1):
            if arr[p - 1] <= arr[q]:
                continue

            arr[p - 1], arr[q] = arr[q], arr[p - 1]
            r = length - 1
            while p < r:
                arr[p], arr[r] = arr[r], arr[p]
                p += 1
                r -= 1

            return True

    return False
