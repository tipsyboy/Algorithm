# https://www.acmicpc.net/problem/21939

import sys
from heapq import heappush, heappop

input = sys.stdin.readline

N = int(input())
lo, hi = [], []

for _ in range(N):
    num, lv = map(int, input().split())
    heappush(lo, (lv, num))
    heappush(hi, (-lv, -num))

M = int(input())
solved_set = set()
for _ in range(M):
    command, *nums = input().split()

    if command == "add":
        num, lv = map(int, nums)
        if num in solved_set:
            while hi and -hi[0][1] in solved_set:
                heappop(hi)
            while lo and lo[0][1] in solved_set:
                heappop(lo)
            solved_set.remove(num)
        heappush(lo, (lv, num))
        heappush(hi, (-lv, -num))
    elif command == "recommend":
        rcmm = -1
        if nums[0] == "1":
            while hi and -hi[0][1] in solved_set:
                heappop(hi)
            rcmm = -hi[0][1]
        else:
            while lo and lo[0][1] in solved_set:
                heappop(lo)
            rcmm = lo[0][1]
        print(rcmm)
    elif command == "solved":
        solved_set.add(int(nums[0]))

    # print(hi)
    # print(lo)