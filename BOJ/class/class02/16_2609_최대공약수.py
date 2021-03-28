def gcd_Euclid(a, b):
    if b == 0:
        return a

    return gcd_Euclid(b, a % b)


def lcm(a, b):
    gcd = gcd_Euclid(a, b)

    return int(a * b / gcd)


a, b = map(int, input().split())

print(gcd_Euclid(a, b))
print(lcm(a, b))
