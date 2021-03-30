n = int(input())
people = []
rank = []

for _ in range(n):
    h, w = map(int, input().split())
    people.append((h, w))

for i in range(n):
    count = 1
    for j in range(n):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            count += 1

    rank.append(count)

for r in rank:
    print(r, end=" ")
