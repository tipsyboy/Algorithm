
import sys

T = int(sys.stdin.readline())

for i in range(T):
    rpt, word = input().split()
    rpt = int(rpt)

    for j in word:
        print(j * rpt, end="")

    print()
