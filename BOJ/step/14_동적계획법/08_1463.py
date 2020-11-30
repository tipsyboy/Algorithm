# import sys

# n = int(sys.stdin.readline())

# make_one = [0] * (n+1)  # n+1개 list

# for i in range(2, n+1):
#     candidate = []

#     if i % 3 == 0:
#         candidate.append(make_one[i//3] + 1)
#     if i % 2 == 0:
#         candidate.append(make_one[i//2] + 1)
#     candidate.append(make_one[i-1] + 1)

#     make_one[i] = min(candidate)

# print(make_one[n])


import sys

candidate = [int(sys.stdin.readline())]
cnt = 0

while 1 not in candidate:
    cnt += 1
    temp = set()
    for elem in candidate:
        if elem % 3 == 0:
            temp.add(elem//3)
        if elem % 2 == 0:
            temp.add(elem//2)
        temp.add(elem-1)
        print(f"temp: {temp}")
    candidate = temp
    print(f"candidate: {candidate}")

print(cnt)
