# 1번 

import sys

N = int(sys.stdin.readline())
As = list(map(int, sys.stdin.readline().split()))

As.sort()

print(As[0], As[-1])

