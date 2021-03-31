import sys
input = sys.stdin.readline

# 1) in 연산자를 사용한 원소 찾기
# 이 경우에 a_list를 list 자료형으로 선언하면 in 연산을 수행하는데 시간 복잡도가 O(n) 되서 시간초과가 남
# set() 자료형은 in 연산에 시간 복잡도가 O(1)로 탐색의 경우 set을 사용하는 편이 더 낫다.

# n = int(input())
# a_list = set(map(int, input().split()))

# m = int(input())
# b_list = map(int, input().split())

# for b in b_list:
#     if b in a_list:
#         print("1")
#     else:
#         print("0")


# 2) 이진 탐색
def binary_search(sorted_list, target, start, end):
    if start > end:
        return 0

    mid = (start + end) // 2

    if sorted_list[mid] == target:
        return 1
    elif sorted_list[mid] > target:
        return binary_search(sorted_list, target, start, mid - 1)
    else:
        return binary_search(sorted_list, target, mid + 1, end)


n = int(input())
a_list = sorted(map(int, input().split()))
m = int(input())
b_list = map(int, input().split())

for b in b_list:
    print(binary_search(a_list, b, 0, n - 1))
