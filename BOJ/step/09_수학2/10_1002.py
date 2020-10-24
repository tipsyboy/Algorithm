# Missile turret

import sys

t_case = int(sys.stdin.readline())

for i in range(t_case):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())

    dist = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5  # 두 점 사이의 거리
    R = max(r1, r2)  # 큰 원
    r = min(r1, r2)  # 작은 원

    # 두 원이 일치하는 경우 (접점 무한)
    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
        continue

    if R-r < dist < R+r:  # 두 점에서 만나는 경우
        print(2)
    elif dist == R+r or dist == R-r:  # 한 점에서 만나는 경우 (접한다.)
        print(1)
    else:  # 만나지 않는 경우
        print(0)

