# euclid geometry  and taxicab Geometry

import sys
from math import pi

r = float(sys.stdin.readline())  # 반지름 r

# 소수점 4자리까지 출력
print(round(pi*r*r, 4))
print(round(2*r*r, 4))
