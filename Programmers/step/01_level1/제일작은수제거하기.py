def solution(arr):
    del arr[arr.index(min(arr))]
    # arr.remove(min(arr))

    if not arr:
        arr.append(-1)

    # 공백 리스트 검사 - 슬라이싱 리턴값 == 리스트
    # if arr[:-1] == []:
    #     arr.append(-1)

    print(arr)

    return arr


solution([4, 3, 2, 1])
solution([10])


### 리스트의 순서가 변경되면 안됨
