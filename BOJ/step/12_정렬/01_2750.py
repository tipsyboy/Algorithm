import sys

N = int(sys.stdin.readline())

sorted_list = []

for i in range(N):
    sorted_list.append(int(sys.stdin.readline()))

sorted_list.sort()

for num in sorted_list:
    print(num)
