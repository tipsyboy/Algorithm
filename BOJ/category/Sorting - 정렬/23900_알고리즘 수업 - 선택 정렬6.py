import sys

input = sys.stdin.readline


def selection_sort(N: int, A: list, B: list) -> bool:
    if A == B:
        return True

    idx_dict = dict()
    for i in range(N):
        idx_dict[A[i]] = i
    maxv_list = sorted(A)

    for i in range(N - 1, 0, -1):
        maxv = maxv_list[i]
        if maxv > A[i]:
            idx_dict[A[i]], idx_dict[maxv] = idx_dict[maxv], idx_dict[A[i]]
            A[idx_dict[A[i]]], A[idx_dict[maxv]] = A[idx_dict[maxv]], A[idx_dict[A[i]]]
            if A == B:
                return True

    return False


N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(1) if selection_sort(N, A, B) else print(0)


"""
23883. 알고리즘 수업 - 선택 정렬3
    - 선택 정렬의 교환 순서를 알기 위해 정렬을 해야하는...

    - 오름차순 선택정렬은 뒤에서 부터 매번 자리마다 가장 큰 값을 선택해서 바꿔주는 정렬로
      nlogn 정렬을 통해서 이번 차례에 들어갈 가장 큰 값을 선택하고
      dict()를 활용해 이전 위치를 저장해가면서 선택정렬을 사용하면 된다. 
    
    - 같은 이름의 3번문제와 풀이 방식은 같고 출력이 다름
"""