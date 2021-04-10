n = int(input())
fear = list(map(int, input().split()))

fear.sort()

team = 0
count = 0
for x in fear:
    count += 1
    if count >= x:
        team += 1
        count = 0

print(team)
