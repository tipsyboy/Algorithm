# Pythagoras's theorem
import sys

while True:
    t_side = list(map(int, sys.stdin.readline().split()))

    if sum(t_side) == 0:
        break

    max_side = max(t_side)
    t_side.remove(max_side)

    if max_side**2 == (t_side[0]**2 + t_side[1]**2):
        print("right")
    else:
        print("wrong")
